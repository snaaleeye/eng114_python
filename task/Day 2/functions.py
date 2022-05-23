from typing import Dict, List

# def print_something(print_string):
#     print(print_string)
#
#
# print_something("Hello World")

# def greeting(name):
#     print("Hello, my name is " + name)
#
# greeting("Sharmake")

# def addition(int1, int2):
#     return int1 + int2

# def multi_args(*multiargs):
#      print(type(multiargs))
#
#      for arg in multiargs:
#          print(arg)
#
# multi_args(1, 2, 3, 4, 5, 6, 100, 2020)

# def greeting(name: int):
#     print("Hello, my name is " + name)
#
#
# greeting(24601) #issue with dynamic programmes - no warning that this won't work.

# def division(denom: int, num: int) -> float:
#     return denom / num
#
#
# def subtraction(int1: int = 5, int2 = 2) -> int:
#     return int1 - int2
#
#
# a: complex = 10
# b: int = 7
#
#
# print(subtraction(10, 7))

# name = List[str] = ["Tom", "Dick", "Harry"]
# options  = Dict[str, bool] = {"subtitles": True, "colourblind_mode": False}

# # Create a calculator
#
# def addition(int1, int2):
#     return int1 + int2
#
#
# def subtraction(int1, int2):
#     return int1 - int2
#
#
# def multiplication(int1, int2):
#     return int1 * int2
#
#
# def division(int1, int2):
#     return int1 / int2
#
#
# print("Select Operation")
# print("1. Addition")
# print("2. Subtraction")
# print("3. Multiplication")
# print("4. Division")
#
# while True:
#     choice = input("Enter Operation")
#     if choice in ('1', '2', '3', '4'):
#         int1 = float(input("Enter first number: "))
#         int2 = float(input("Enter second number: "))
#
#         if choice == '1':
#             print(int1, "+", int2, "=", addition(int1, int2))
#
#         elif choice == '2':
#             print(int1, "-", int2, "=", subtraction(int1, int2))
#
#         elif choice == '3':
#             print(int1, "*", int2, "=", multiplication(int1, int2))
#
#         elif choice == '4':
#             print(int1, "/", int2, "=", division(int1, int2))
#
#         next_calculation = input("Let's do next calculation? (yes/no): ")
#         if next_calculation == "no":
#             break
#
#     else:
#         print("Invalid Input")


