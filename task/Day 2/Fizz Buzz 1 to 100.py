# Fizz Buzz Task

# Core
# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number.
# For multiples of five print "Buzz" instead of the number
# For numbers which are multiples of both three and five print "FizzBuzz"

# Extra
# make a new fizzbuzz file and make it functional
# make it so we can decide which numbers to substitute for fizz and buzz using functions.

for i in range(1, 101):
    if (i%15 == 0):
        print("FizzBuzz")

    elif (i%3 == 0):
        print("Fizz")

    elif(i%5 == 0):
        print("Buzz")

    else:
        print(i)