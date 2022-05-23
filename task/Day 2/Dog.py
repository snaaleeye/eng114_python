# # benefits- no conflicts - self-contained.
# # Instantiation -sets local version of class.
# class Dog:
#
#     animal_kind = "canine" # class variable which returns an attribute of a string
#
#     def bark(self): # method not a function
#         return "woof"

# #print(Dog.animal_kind)
# #print(Dog.bark())
#
# fido = Dog()
# lassie = Dog()
# rex = Dog()
# daisy = Dog()
# tom = Dog()
#
# lassie.breed = "Golden Retriever"
# rex.breed = "Germany Shepherd"
# daisy.breed = "Bull dog"
# fido.breed = "Jack Russell"
#
# print(type(fido.breed))
# print(type(lassie.breed))
# print(rex.breed)
# print(daisy.breed)
# print(tom.breed)

# Initialisation


# class Dog:
#
#
#     def __init__(self, name, colour): # Dunder underscroll.
#         self.animal_kind = "canine"
#         self.name = name
#         self.colour = colour
#         self.bark()
#
#     def bark(self): # method not a function
#         return "woof"
#
#
# fido = Dog("lassie", "golden") # this speeds up process - cutting down redundancies
#
# print(fido.name)
# print(fido.colour)
#
