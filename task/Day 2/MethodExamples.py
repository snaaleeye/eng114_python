# class MethodExamples:
#
#     def __init__(self):
#         self.this_can_be_accessed_easily = "Hi, here I am easily found"
#
#     def get_this_can_be_accessed_easily(self):
#         return self.this_can_be_accessed_easily
#
#     def set_this_can_be_accessed_easily(self, value_to_be_set):
#          self.this_can_be_accessed_easily = value_to_be_set
#
#
# x = MethodExamples() #Instantiation
#
#
# x.this_can_be_accessed_easily
#
# # print(x.this_can_be_accessed_easily)
# # x.this_can_be_accessed_easily = "I have changed"
# # print(x.this_can_be_accessed_easily)
#
# # What to do if we wanted it hidden. Getters and Setters. Python lets you see everything . No private/public.
# # Underscore = access to protective member. Hidden. 1 Underscore protected 2 is hidden.
# #Some argue setters and getters are redundant -
#
# print(x.this_can_be_accessed_easily)
# x.set_this_can_be_accessed_easily("I have changed")
# print(x.this_can_be_accessed_easily)

# Task
# Create car class
# Give vehicle a maximum speed + keep track of the current speed
# adjust the speed directly using speed getter
# Does breaking past 0 cause the speed to increase?
# Can you accelerate past the top speed?

#
# class Car:
#
#     def __init__(self, model, top_speed, current_speed):
#         self.__model = model
#         self.__top_speed = top_speed
#         self.__current_speed = current_speed
#
#
#     def set_speed(self, speed):
#         self.__speed = 0
#
#
#     def get_speed(self):
#         return self.__speed
#
#
#     def accelerate(self):
#         self.__speed +=5
#
#
#     def brake(self):
#         self.__speed -=5
#
#
#     def get_speed(self):
#         return self.__speed
#
#
# def main(mycar=None):
#
#     model = mycar
#     top_speed = 100
#     current_speed = 20
#
#     mycar = Car(model, top_speed, current_speed)
#
#
#     mycar.accelerate()
#     print('The current speed is: ', mycar.get_speed())
#     mycar.accelerate()
#     print('The current speed is: ', mycar.get_speed())
#     mycar.accelerate()
#     print('The current speed is: ', mycar.get_speed())
#     mycar.accelerate()
#
#
#     mycar.brake()
#     print('The current speed after brake is: ', mycar.get_speed())
#     mycar.brake()
#     print('The current speed after brake is: ', mycar.get_speed())
#     mycar.brake()
#     print('The current speed after brake is: ', mycar.get_speed())
#     mycar.brake()
#
# main()

# Florent's code

class Car:
    def __init__(self, model, top_speed, current_speed):
        self.model = model
        self.top_speed = top_speed
        self.current_speed = current_speed

    def set_increase_current_speed(self):
        if self.current_speed > self.top_speed - 5:
            print("fCurrent speed - {self.current_speed}mph - cannot exceed top speed which is {self.top_speed}mph")
        else:
            self.current_speed += 5

    def set_decrease_current_speed(self):
        if self.current_speed < 5:
            print("Speed cannot be negative")
        else:
            self.current_speed -= 5

def mycar():

    model = "Tesla"
    top_speed = 100
    current_speed = 20

    mycar = Car(model, top_speed, current_speed)


    mycar.set_increase_current_speed()
    print("The current speed is", mycar.current_speed())
    mycar.set_increase_current_speed()
    print('The current speed is: ', mycar.current_speed())
    mycar.set_increase_current_speed()
    print('The current speed is: ', mycar.current_speed())
    mycar.set_increase_current_speed()


    mycar.set_decrease_current_speed()
    print('The current speed after brake is: ', mycar.get_speed())
    mycar.set_decrease_current_speed()
    print('The current speed after brake is: ', mycar.get_speed())
    mycar.set_decrease_current_speed()
    print('The current speed after brake is: ', mycar.get_speed())
    mycar.set_decrease_current_speed()

mycar()