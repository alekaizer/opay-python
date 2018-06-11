

class Settings:
    def __init__(self, public_key, private_key, reference, mode):
        self.api_key = public_key
        self.secret_key = private_key
        self.merchant_reference = reference

        if mode == "test":
            self.url = "https://bz-sandbox.opay-test.net/api/"
        else:
            self.url = "https://operapay.com/api/"
        self.access_code = 'access/code'
        self.access_token = 'access/token'
        self.gateway_create = "gateway/create"
        self.gateway_commit = "gateway/commit"
        self.gateway_status = "gateway/status"
        self.gateway_3dsecure = "gateway/3dsecure"
        self.gateway_input_otp = "gateway/input-otp"
        self.gateway_input_pin = "gateway/input-pin"
        self.gateway_bank_fields = "gateway/bank-fields"
        self.lookup_bank_account = "lookup/bank-account"
        self.resource_banks = "lookup/banks"
        self.payment_order = "payment/order"
        self.account_verification = "/v1/resolve/account"
        self.card_tokenization = "/v1/transfer/charge/tokenize/card"
        self.card_enquiry = "/v1/user/card/check"
        self.reporting = "/v1/report/transactions"
        self.transaction_get_total = "/v1/get-charge"
        self.transaction_retrial = "/v1/transfer/disburse/retry"
        self.transaction_previous_card = "/v1/transfer/{0}"
        self.transaction_status = "/v1/transfer/charge/status"
        self.transaction_wallet = "/v1/disburse/status"

