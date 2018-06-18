from opay.bank import Bank
from opay.charge import Charge
from opay.gateway import Gateway
from opay.utils.settings import Settings
from opay.utils.utils import Util


class Opay:
    def __init__(self, public_key, private_key, env="test"):
        self.settings = Settings(public_key, private_key, env)
        self.__util = Util(self.settings)
        self.Gateway = Gateway(self.__util)
        self.Bank = Bank(self.__util)
        self.Charge = Charge(self.__util)

