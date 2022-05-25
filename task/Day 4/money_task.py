

class money_exchange:

    def __init__(self, money_exchange):
        self.money_exchange = money_exchange

    def __format__(self, format_spec):
        if format_spec == "money":
            return f"Your Total is £{self.money_exchange}"
        else:
            return f"Your total is ${self.money_exchange * 1.15}"

check_flag = True
amount = int(input("Please enter how much money you have in dollars"))

while check_flag:
    if amount <= 0:
        amount = int(input("please enter a positive value "))

    elif amount > 0:
        currency = "${:,.2f}".format(amount)
        print(currency)
        check_flag = False
        break
    else:
        amount = int(input("please enter a value"))


customer_1 = money_exchange(23)
print(f"{customer_1}")
print(f"{customer_1:money}")