# for i in range(1, 101):
#     if (i%15 == 0):
#         print("FizzBuzz")
#
#     elif (i%3 == 0):
#         print("Fizz")
#
#     elif(i%5 == 0):
#         print("Buzz")
#
#     else:
#         print(i)

# class Fizzbuzz:
#
#     def __init__(self, start_of_range, end_of_range):
#         self.fizzrange = range(start_of_range, end_of_range)
#         self.fizzbuzz_list = []
#         self._fizzbuz_iterator()
    #
    #
    # def _divisible_by(self, num1, num2):
    #     if num1 % num2 == 0:
    #         return True
    #     else:
    #         return False
    #
    #
    # def _fizzbuzz_iterator(self):
    #
    #     for num in self.fizzrange:
    #         if self._divisible_by(num, 15):
    #             self.fizzbuzz_list.append("fizzbuzz")
    #         elif self._divisible_by(num, 5):
    #             self.fizzbuzz_list.append("buzz")
    #         elif self._divisible_by(num, 3):
    #             self.fizzbuzz_list.append("fizz")
    #         else:
    #             self.fizzbuzz_list.append(num)