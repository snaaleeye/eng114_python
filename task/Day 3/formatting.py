# class Location:
#     def __init__(self, latitude, longitude):
#         self.latitude = latitude
#         self.longitude = longitude
#
#
#     def __repr__(self):
#         return f"Location(latitude={self.latitude}, longitude={self.longitude})"
#
#     def __str__(self): #user friendly version in a more readable way
#         return f"({self.latitude}, {self.longitude})"
#
# bham_academy = Location(52.488647, -1.887249)
# print(bham_academy)

# n = 0.004837
#
# print(f"Fixed Point: {n:f}")
# print(f"Exponential Notation: {n:e}")

# class Dog:
#     def __init__(self, age):
#         self.age = age
#
#     def __str__(self):
#         return f"A {self.age} year old Dog"
#
#     def __format__(self, format_spec):
#         if format_spec == "dog":
#             return f"A {self.age * 7} dog-years old Dog"
#         else:
#             return self.__str__()
#
#
# fido = Dog(5)
# print(f"{fido}")
# print(f"{fido:dog}")

#  Create application - input numbers - currency
# £10.00 two decimal places.
#
# class Currency:
#     def __init__(self, GBP, USD):
#         self.GBP = GBP
#         self.USD = USD
#
# GBP = Currency(1)
# USD = Currency(1.5)
#
# user_input = input(int())
#
# print(f"You have {(user_input}%1.15 dollars")


# check_flag = True
# amount = int(input("please enter the amount of money"))
#
# while check_flag:
#     if amount <= 0:
#         amount = int(input("please enter a positive value "))
#
#     elif amount > 0:
#         currency = "${:,.2f}".format(amount)
#         print(currency)
#         check_flag = False
#         break
#     else:
#         amount = int(input("please enter a value"))
#
# class Money:
#     def __init__(self, money):
#         self.money = money
#
#
#     def __format__(self, format_spec):
#         if format_spec == "money":
#             return f"The Total is £{self.money}"
#         else:
#             return f"The total is ${self.money * 1.15}"
#
#
# customer_1 = Money(50)
# print(f"{customer_1}")
# print(f"{customer_1:money}")