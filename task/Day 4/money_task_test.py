from money_exchange import Money_Exchange
import unittest

class money_exchange:

    def __init__(self, money_exchange):
        self.money_exchange = money_exchange

    def __format__(self, format_spec):
        if format_spec == "money":
            return f"Your Total is £{self.money_exchange}"
        else:
            return f"Your total is ${self.money_exchange * 1.15}"