class Bank:
    def __init__(self, util):
        self.util = util

    def disburse(self, amount, recipient_account, recipient_bank_code,
                 recipient_phone_number=None, recipient_email=None):
        data = {
           "orderConfig": {
              "serviceType": "bank",
              "recipientAccount": recipient_account,
              "recipientBankCode": recipient_bank_code,
              "paymentAmount": amount,
              "currencyISO": "NGN",
              "countryCode": "NG",
              "instruments": [
                 {
                    "type": "coins"
                 }
              ]
           }
        }

        if recipient_phone_number:
            data["customerPhone"] = recipient_phone_number
        if recipient_email:
            data["customerEmail"] = recipient_email

        r = self.util.send_request(self.util.settings.payment_order, data)
        if 'orderWithStatus' in r:
            return r.get('orderWithStatus')
        else:
            return r