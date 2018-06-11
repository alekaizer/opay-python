class Charge:
    def __init__(self, util):
        self.util = util

    def make_payment(self, amount, instrument_id):
        data = {
           "orderConfig": {
              "serviceType": "gateway",
              "paymentAmount": amount,
              "currencyISO": "NGN",
              "countryCode": "NG",
              "instruments": [
                 {
                    "type": "token",
                    "id": instrument_id
                 }
              ]
           }
        }

        r = self.util.send_request(self.util.settings.gateway_status, data)
        if 'orderWithStatus' in r:
            return r.get('orderWithStatus')
        else:
            return r