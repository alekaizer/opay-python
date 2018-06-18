import base64
import json

import requests
from Crypto.Cipher import DES3
from datetime import datetime
import random
import string

redis = {}


class Util:
    def __init__(self, settings):
        self.settings = settings
        self.__get_auth()

    def __get_auth(self):
        headers = {"Accept": "application/json",
                   "Content-type": "application/json"}

        response = requests.post(self.resolve_url(self.settings.access_code),
                                 headers=headers,
                                 data=json.dumps(
                                     {"publicKey": self.settings.api_key})
                                 )
        if response.status_code == 200:
            body = response.json()
            if 'data' in body:
                print(body)
                access_code = body.get('data').get('accessCode')
                response = requests.post(
                    self.resolve_url(self.settings.access_token),
                    headers=headers,
                    data=json.dumps({"accessCode": access_code,
                                     "privateKey": self.settings.secret_key})
                )
                if response.status_code == 200:
                    body = response.json()
                    if 'data' in body:
                        self.token = body.get('data').get('accessToken'
                                                          ).get('value')
                    print("new token", self.token)
                    redis["opay:latest"] = datetime.now().timestamp()
                else:
                    self.token = None
                    raise Exception("server",
                                    response.json())
        else:
            self.token = None
            print()
            raise Exception("server " + str(response.status_code),
                            response.json())

    def resolve_url(self, endpoint):
        return self.settings.url + endpoint

    def send_request(self, endpoint, data, method="post"):
        latest_token = redis.get("opay:latest")
        if latest_token:
            l = redis.get("opay:latest")
            delta = datetime.now().timestamp() - l
            if delta > 3500:
                self.__get_auth()
                redis["opay:latest"] = datetime.now().timestamp()
        headers = {"Accept": "application/json",
                   "Authorization": self.token}
        if method == "get":
            req = requests.get(self.resolve_url(endpoint), headers=headers)
        else:
            req = requests.post(self.resolve_url(endpoint), data=json.dumps(data),
                                headers=headers)
        if req.status_code == 200:
            body = req.json()
            if 'data' in body and body.get('data'):
                return body.get('data')
            else:
                return {'status': 'error',
                        'message': body.get('errors')[0].get('message'),
                        "response": req.json()}
        else:
            body = req.json()
            return {"status": "error",
                    "response": body}

    def encrypt(self, message):

        block_size = 8
        padding_size = block_size - (len(message) % block_size)

        if padding_size > 0:
            message += chr(padding_size) * padding_size
        cipher = DES3.new(message, DES3.MODE_ECB)
        ciphered = cipher.encrypt(message.encode('utf-8'))
        return base64.b64encode(ciphered).decode('utf-8')


def random_name():
    char_set = string.ascii_uppercase + string.digits + string.ascii_lowercase
    return ''.join(random.sample(char_set * 10, 20))
