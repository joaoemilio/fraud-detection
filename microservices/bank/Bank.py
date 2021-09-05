import json
from flask import current_app
from Utility import Utility

class Bank():

    def __init__(self):
        self.util = Utility()

    def payment(self):
        c = "joaoemilio"
        m = "merchant1"
        self.util.info(f"processing payment for customer={c} merchant={m}")
        return { "response": "payment" }

    def debit(self):
        c = "joaoemilio"
        self.util.info(f"processing debit for customer={c}")
        return { "response": "debit" }

    def cashin(self):
        c = "joaoemilio"
        self.util.info(f"processing cash in for customer={c}")
        return { "response": "cash in" }

    def cashout(self):
        c = "joaoemilio"
        self.util.info(f"processing cash out for customer={c}")
        return { "response": "cash out" }

    def transfer(self):
        c = "joaoemilio"
        self.util.info(f"processing transfer for customer={c}")
        return { "response": "transfer" }


