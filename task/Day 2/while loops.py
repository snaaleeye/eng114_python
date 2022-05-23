# x = 0
#
# #while x < 10:
# #    print(f"it's working -> {x}")
# #    x += 1
#
# while x < 10:
#     print(f"it's working -> {x}")
#     if x == 4:
#         break # break may only occur syntactically nested in a for or while loop, but not nested in a function or class definition within that loop.
# #It terminates the nearest enclosing loop, skipping the optional else clause if the loop has one.
# #If a for loop is terminated by break, the loop control target keeps its current value.
# #When break passes control out of a try statement with a finally clause, that finally clause is executed before really leaving the loop.
#     x += 1

# age = input("What is your age")
# print(f"Your age is {age}")

# user_prompt = True
#
# while user_prompt:
#     age = input("What is your age")
#     if age.isdigit():
#         user_prompt = False
#     else:
#         print("Please provide your answer in digits")
#
# # print(f"Your age is {age}")
# # This above results in an infinite loop if space is used.
#
# # Create a conditional programme - Create password system
# # Email and Password
# # Must input email and password - if they put anything that error and eep them in it
# # A loop within a loop if password and email are correct then exit loop.
# # Add date/time
#
# import datetime
# date = datetime.datetime.now()
#
# user = {1: {"email": "sparta@spartaglobal.com", "password": "sparta"}}
#
# found = False
# while not found:
#     email_input = input("Please enter your email address")
#     password_input = input("Please enter your password")
#
#     for key, info in user.items():
#         if email_input == info["email"] and password_input == info["password"]:
#             found = True
#             break
#     else:
#         print("Error Incorrect Email or Password or Both")
#
# print(f"You have successfully logged in")
#
#
# email = "sparta@spartaglobal.com"
# password = "1234"
#
# loop active = True
#
# while loop active:
#     input_email = input("Enter your email")
#     if email.lower() == input_email.lower():
#         print("Email found")
#         while loop_active:
#             input_password = input("Enter your password")
#             if password == input_password:
#                 print("Login successful")
#                 loop_active = False
#     else:
#         print("Please enter the correct email: ")
#
# print("Login successful")
