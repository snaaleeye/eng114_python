shopping_list = ["eggs", "bread", "bananas", "biscuits", "milk"]


print(shopping_list[-1])
print(shopping_list[-1])

shopping_list[0] = "sugar"

print(shopping_list[0])
print(len(shopping_list))

shopping_list.append["carrots"]

print(shopping_list)
print(len(shopping_list))

shopping_list.pop() removes last item on the list

mixture = [1, 2, 3, "one", "two", "three"]

print(mixture[1:3])
print(mixture[-2::])
print(mixture::2)

essentials = ("bread", "eggs","milk" ) a list is mutable - tuples are not
print(essentials)
print(essentials.count("bread"))

Dictionary
student_1 = {
    "name":"susan",
    "stream": "tech",
    "completed_lessons": 4
   "completed_lesson_names": ["variables", "data_types", "set up" ]
}

print(student_1["stream"]) returns stream from dictionary
print(student_1["completed_lesson_names"][0])

student_1["completed_lessons"] = 3
print(student_1["completed_lessons"])

car_parts = {"wheels", "doors", "exhaust"}
car_parts.add("windows")
car_parts.discard("doors")
print(car_parts)

frozen set immutable - immutable = not changeable

x = frozenset([1, 2, 3, 4])
