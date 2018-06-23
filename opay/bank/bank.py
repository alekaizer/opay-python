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

    def check_account(self, account_number, bank_code):
        data = {
            "bankCode": bank_code,
            "accountNumber": account_number,
            "countryCode": "NG"
        }

        r = self.util.send_request(self.util.settings.lookup_bank_account, data)

        if 'data' in r and 'lookupBankAccount' in r:
            return r.get('data')
        else:
            return r

    def get_banks(self):
        return [
                {"Code": "232150029", "Country": "NG", "Name": "Sterling Bank"},
                {"Code": "057150013", "Country": "NG", "Name": "Zenith Bank"},
                {"Code": "044150149", "Country": "NG", "Name": "Access Bank"},
                {"Code": "035150103", "Country": "NG", "Name": "Wema Bank"},
                {"Code": "063150162", "Country": "NG", "Name": "Diamond Bank"},
                {"Code": "070150003", "Country": "NG", "Name": "Fidelity Bank"},
                {"Code": "058152052", "Country": "NG", "Name": "Gt Bank"},
                {"Code": "011152303", "Country": "NG", "Name": "First Bank"},
                {"Code": "050150311", "Country": "NG", "Name": "EcoBank"},
                {"Code": "084150015", "Country": "NG", "Name": "Enterprise Bank"},
                {"Code": "214150018", "Country": "NG", "Name": "Fcm Bank"},
                {"Code": "030159992", "Country": "NG", "Name": "Heritage Bank"},
                {"Code": "301080020", "Country": "NG", "Name": "Jaiz Bank"},
                {"Code": "082150017", "Country": "NG", "Name": "Keystone Bank"},
                {"Code": "014150030", "Country": "NG", "Name": "MainStreet Bank"},
                {"Code": "023150005", "Country": "NG", "Name": "Citi Bank"},
                {"Code": "076151006", "Country": "NG", "Name": "Skye Bank"},
                {"Code": "221159522", "Country": "NG", "Name": "Stanbic Bank"},
                {"Code": "068150057", "Country": "NG", "Name": "Standard Bank"},
                {"Code": "032156825", "Country": "NG", "Name": "Union Bank"},
                {"Code": "033154282", "Country": "NG", "Name": "Uba Bank"},
                {"Code": "215082334", "Country": "NG", "Name": "Unity Bank"},
                {"Code": "101000000", "Country": "NG", "Name": "Providus Bank"}
        ]
