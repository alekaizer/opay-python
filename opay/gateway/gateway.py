class Gateway:
    def __init__(self, util):
        self.util = util

    def create(self, card, amount=10):
        data = {
            "input": {
                "currency": "NGN",
                "publicKey": self.util.settings.api_key,
                "amount": amount,
                "reference": self.util.settings.merchant_reference,
                "countryCode": "NG",
                "tokenize": True,
                "instrumentType": "card",
                "cardNumber": card.number,
                "cardDateMonth": card.month,
                "cardDateYear": card.year,
                "cardCVC": card.cvv
            }
        }
        r = self.util.send_request(self.util.settings.gateway_create, data)
        if 'gatewayCreate' in r:
            return r.get('gatewayCreate')
        else:
            return r

    def tokenize_card(self, card):
        data = {
            "input": {
                "currency": "NGN",
                "publicKey": self.util.settings.api_key,
                "amount": 10,
                "reference": self.util.settings.merchant_reference,
                "countryCode": "NG",
                "tokenize": True,
                "instrumentType": "card",
                "cardNumber": card.number,
                "cardDateMonth": card.month,
                "cardDateYear": card.year,
                "cardCVC": card.cvv
            }
        }
        r = self.util.send_request(self.util.settings.gateway_create, data)
        if 'gatewayCreate' in r:
            return r.get('gatewayCreate')
        else:
            return r

    def tokenize_bank(self, account_number, bank_name):
        data = {
            "input": {
                "currency": "NGN",
                "publicKey": self.util.settings.api_key,
                "amount": 10,
                "reference": self.util.settings.merchant_reference,
                "countryCode": "NG",
                "tokenize": False,
                "instrumentType": "account",
                "senderAccountNumber": account_number,
                "bank": bank_name
            }
        }
        r = self.util.send_request(self.util.settings.gateway_create, data)
        if 'gatewayCreate' in r:
            return r.get('gatewayCreate')
        else:
            return r

    def commit(self, amount, transaction_token):
        data = {
            "input": {
                "currency": "NGN",
                "privateKey": self.util.token,
                "amount": amount,
                "countryCode": "NG",
                "token": transaction_token
            }
        }
        r = self.util.send_request(self.util.settings.gateway_create, data)
        if 'gatewayCommit' in r:
            return r.get('gatewayCommit')
        else:
            return r

    def get_status(self, transaction_token):
        data = {
            "token": transaction_token
        }
        r = self.util.send_request(self.util.settings.gateway_status, data)
        if 'gatewayStatus' in r:
            return r.get('gatewayStatus')
        else:
            return r

    def get_3dS_link(self, transaction_token):
        data = {
            "token": transaction_token
        }
        r = self.util.send_request(self.util.settings.gateway_status, data)
        if 'gateway3DSecure' in r:
            return r.get('gateway3DSecure')
        else:
            return r

    def set_otp(self, transaction_token, otp):
        data = {
            "token": transaction_token,
            "otp": otp
        }
        r = self.util.send_request(self.util.settings.gateway_status, data)
        if 'gatewayInputOTP' in r:
            return r.get('gatewayInputOTP')
        else:
            return r

    def set_pin(self, transaction_token, pin):
        data = {
            "token": transaction_token,
            "pin": pin
        }
        r = self.util.send_request(self.util.settings.gateway_status, data)
        if 'gatewayInputPIN' in r:
            return r.get('gatewayInputPIN')
        else:
            return r

    def get_bank_required_fields(self, bank_name):
        data = {
            "bank": bank_name
        }
        r = self.util.send_request(self.util.settings.gateway_status, data)
        if 'gatewayBankPaymentFields' in r:
            return r.get('gatewayBankPaymentFields')
        else:
            return r
