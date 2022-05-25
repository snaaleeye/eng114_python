# Python Fundamentals

* Data Types

Text Type:	str

Numeric Types:	int, float, complex

Sequence Types:	list, tuple, range

Mapping Type:	dict

Set Types:	set, frozenset

Boolean Type:	bool

Binary Types:	bytes, bytearray, memoryview

None Type:	NoneType 

Int - Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

Float - Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

Complex - Complex numbers are written with a "j" as the imaginary part:

Type Conversion - You can convert from one type to another with the int(), float(), and complex() methods:

Random Number - Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:

List is a collection which is ordered and changeable. Allows duplicate members.

Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.

Dictionary is a collection which is ordered** and changeable. No duplicate members


* Variables

Python has no command for declaring a variable.

A variable is created the moment you first assign a value to it. 

Casting can specify the data type of a variable. e.g.
x = str(3) # x will be '3'
y = int(3) # y will be 3
z = float(3) # z will be 3.0

type() function is used to get the data type.
x = 5
y = "John"
print(type(x)) # <class 'int'>
print(type(y)) # <class 'str'>

Variable names are case-sensitive

Python allows you to extract the values as variables. 
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

 Variable - a declaration of value that can be changed.
 Good for skeleton code

a = 1 int
b = 2 int
c = 3.5 float

hi = "hello world!" string

print(type(hi))
print(type(a))
print(type(b))

a = input("Please enter the value of a")
print(a)

name = "Mark"
age = "24"
DOB = "10/09/1997"

print(name)
print(age)
print(DOB)

name = input("Please enter your name")
age = input("Please enter your age")
DOB = input("Please enter your Date of Birth")
height_cm = input("Please input height")
Address = input("Please enter where you live")
film = input("Please enter your favourite film")
food = input("Please enter your favourite food")

print(f" Your name is {name}. You are {age} old.  You are {height_cm} tall. Your date of birth is {DOB}. Your favourite film is {film}. You live in {Address}. Your favourite food is  {food}")

* Strings

int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)

float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)

str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals

len() - to get the length of a string

Slicing - You can return a range of characters by using the slice syntax. Specify the start index and the end index, separated by a colon, to return a part of the string.
b = "Hello, World!"
print(b[2:5])
Negative Indexing
Use negative indexes to start the slice from the end of the string: 
b = "Hello, World!"
print(b[-5:-2])

String Concatenation
To concatenate, or combine, two strings you can use the + operator. 
a = "Hello"
b = "World"
c = a + b
print(c)

Escape characters - To insert characters that are illegal in a string, use an escape character. An escape character is a backslash \ followed by the character you want to insert.

Code	Result	
\'	    Single Quote	
\\	    Backslash	
\n	    New Line	
\r	    Carriage Return	
\t	    Tab	
\b	    Backspace	
\f	    Form Feed	
\ooo	Octal value	
\xhh	Hex value

Single_quotes = 'This works'
Double_quotes = "This also works"

print(Single_quotes)
print(Double_quotes)

Bad_string = 'Wow, I don\t like this
Another_string = 'He said "I dont like this"'
Another_string2 = "He said \"I dont like this\""


Hw = "Hello! World"

print(Hw[7:])
print(Hw[-5])
print(Hw[:5]) after slice
print(Hw[0:5]) range of slice

print(len(Hw)) tells us total length

White_space = "       lot's      of space at the end                 "
print(len(White_space))
print(len(White_space.strip())) gets rid of white space - good for websites so people don't make mistakes

Example_text = "here's some text with lot's of text"
print(Example_text.count("text")) counts how many times the thing is in the string
print(Example_text.lower())
print(Example_text.upper())
print(Example_text.capitalize())
print(Example_text.replace("with ", ","))

email = "ShArMaKE@SpArTAGlo"
print(email.lower())

a = "here  "
b = "more  "
c = "much more"

print(a + b + c)

x = 2
y = 5.4
z = "  there's now a number 25.4 unless we put a space in!"
print(x + y + z) this below work does not work as you cannot concatonise different

print(str(x) + str(y) + z) this still shows an error but will pass it along

int_string = "6"
print(int(int_string)) you can change both to float instead to check if correct
print(type(int(int_string)))

a = "2"
b = "4"
print(a + b) this gives you 24 instead of 6
print(int(a) + int(b)) this is what you do to correct number

 F strings

name = "Sharmake"
years = 11
height_cm = 60.2

print(f"{name} is {years} years old and {height_cm} cm tall.")

name = "Snoopy"
years = 52

print(f"{name.upper()} IS {years * 7} YEARS OLD IN DOG YEARS!")

pi = 3.14159265359

print(f"Pi to 3 decimal places: {pi:.3f}") Pi to 3 decimal places 3.142
print(f"Pi to 5 decimal places: {pi:.5f}") Pi to 5 decimal places

score = 16
max_score = 26

print(f"You scored {score/max_score}")
print(f"You scored {score/max_score:%}")
print(f"You scored {score/max_score:.2%}")
print(f"You scored {score/max_score:.0%}")

print(hello
    )


* Collections

List is a collection which is ordered and changeable. Allows duplicate members.

Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.

Dictionary is a collection which is ordered** and changeable. No duplicate members

Method	   Description
append()   Adds an element at the end of the list
clear()	   Removes all the elements from the list
copy()	   Returns a copy of the list
count()	   Returns the number of elements with the specified value
extend()   Add the elements of a list (or any iterable), to the end of the current list
index()	   Returns the index of the first element with the specified value
insert()   Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()    Removes the item with the specified value
reverse()   Reverses the order of the list
sort()	Sorts the list

Sort List Alphanumerically
List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

Sort Descending
To sort descending, use the keyword argument reverse = True:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

Reverse Order
What if you want to reverse the order of a list, regardless of the alphabet? The reverse() method reverses the current sorting order of the elements. 
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

Join Two Lists. There are several ways to join, or concatenate, two or more lists in Python. One of the easiest ways are by using the + operator. 

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

shopping_list = ["eggs", "bread", "bananas", "biscuits", "milk"]

print(shopping_list[-1])
print(shopping_list[-1])

shopping_list[0] = "sugar"

print(shopping_list[0])
print(len(shopping_list))

shopping_list.append["carrots"] # To add an item to the end of the list, use the append() method

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

Dictionary - Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is ordered*, changeable and do not allow duplicates. Dictionaries are written with curly brackets, and have keys and values:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

Method	     Description
clear()	     Removes all the elements from the dictionary
copy()	     Returns a copy of the dictionary
fromkeys()	 Returns a dictionary with the specified keys and value
get()	     Returns the value of the specified key
items()	     Returns a list containing a tuple for each key value pair
keys()	     Returns a list containing the dictionary's keys
pop()	     Removes the element with the specified key
popitem()	 Removes the last inserted key-value pair
setdefault() Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	 Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary

* Boolean

Most Values are True. Almost any value is evaluated to True if it has some sort of content.
- Any string is True, except empty strings.
- Any number is True, except 0.
- Any list, tuple, set, and dictionary are True, except empty ones.

Some Values are False
In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.

One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:

a = True
b = False

print(a == b) false
print(a != b) true
print(a >= True) true
print(b <= False) true

print(True and False)
print(False and True)
print(False or True)

isalpha checks if its alpha numerical - if its numbers or letters

hi = "Hello World!"

print(hi.isalpha())
print(hi.islower())
print(hi.isupper())
print(hi.endswith("!"))
print(hi.startswith("H"))

true is anything that is not 0
x = 0
y = 10

print(bool(x))
print(bool(y))

 null and none are different to 0. Zero is still a value null does not exist

print(bool(None))

x = None

print(x == False)
print(x == True)
print(x == None)

Create programme - "you give your age and it calculates when you were born""

name = input("Please enter your name")
age = input("Please enter your age")

print(f" Your name is {name}. You were born in {2022 - int(age)} or {2021 - int(age)} .")

from datetime import date
name = input("Please enter your name")
age = input("Please enter your age")
month = input("Please enter your birth month")
day = input("Please enter your birth day")

month > ["January" "February" "March" "April" "May"]
month < ["June" "July" "August" "September" "October" "November" "December"]

2022 == True
2021 == False


if current_date.month < int(month):
    birth_year -=

else:
    birth_year

print(f" Hello Human. Your name is {name}. You were born in .")



def age(name, year, month, day):
    print(f"Hello {name}, nice to meet you!")
    if month <= 5 and day <= 19:
        print("You were born in")
    elif month >= 5 and day >= 19:
        print("You were born in")
    else:
        print("Error with your birthday")

name = input("Please enter your name")
age = input("Please enter your age")
month = input("Please enter your birth month")
day = input("Please enter your birth day")

A = (2022 - int(year))
B = (2021 - int(year))

from datetime import date

age = int(input("What is your age?"))
born_year = this_year - age
print(f"You were born": {born_year})

today = date.today()
age = today.year - birthdate.year - ((today.month, today.day)) < (birthdate.month, birthdate.day)

name = input("Please enter your name")
height = input("Please enter your height")
favourite_colour = input("Please enter your favourite colour")
secret_spirit_animal = input("Please enter your secret spirit animal")

print(f"Hello Human! Your name is {name}. You are {height} tall. Your favourite colour is {favourite_colour}")

print(f"Your secret animal's first letter is {(secret_spirit_animal)[0]}."
      f"Your secret animal's last letter is {(secret_spirit_animal)[-1]}. "
      f"The Secret Spirit Animal has {(len(secret_spirit_animal))} letters.")

guess = input("What is the secret animal?").lower()

if guess == secret_spirit_animal:
    print("Congratulations! You are right")

else:
    print("Better luck next time")

print(Hw[7:])
print(Hw[-5])
print(Hw[:5]) after slice
print(Hw[0:5]) range of slice
print(len(Hw)) tells us total length

* Functions

A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.

A parameter is the variable listed inside the parentheses in the function definition. An argument is the value that is sent to the function when it is called

def my_function():
  print("Hello from a function")


A lambda function is a small anonymous function. A lambda function can take any number of arguments, but can only have one expression.
x = lambda a : a + 10
print(x(5))

DRY - Don't Repeat Yourself.

# Python Object-Oriented Programming

Difference between method and 

Python is an object oriented programming language. Almost everything in Python is an object, with its properties and methods.

A method is a function inside a class. Objects can also contain methods. Methods in objects are functions that belong to the object.


Inheritance - passing it along - allowing to call things externally. Sharing traits - 


The idea of encapsulation - self contained - hiding information - keeping it clean - 


Abstraction - taking complex ideas keeping it surface level 

An iterator is an object that contains a countable number of values. An iterato$

"__init__" is a reseved method in python classes. It is known as a constructor in object oriented concepts. This method called when an object is created from the class and it allow the class to initialize the attributes of a class.

Encapsulation
Encapsulation is accomplished when each object maintains a private state, inside a class. Other objects can not access this state directly, instead, they can only invoke a list of public functions.

Abstraction
Abstraction is an extension of encapsulation. It is the process of selecting data from a larger pool to show only the relevant details to the object. Suppose you want to create a dating application and you are asked to collect all the information about your users.

Inheritance
Inheritance is the ability of one object to acquire some/all properties of another object. For example, a child inherits the traits of their parents. With inheritance, reusability is a major advantage.

Polymorphism
Polymorphism gives us a way to use a class exactly like its parent so there is no confusion with mixing types.

Functions
Functions are a block of reusable code that can preform a specific tasks without repeating.
DRY Don't Repeat Yourself

Test-Driven Development - TDD is a software development practice that focuses on coding, testing (unit testing) and refactoring.

Unit testing is a software testing method by which individual units of source code are put under various tests to determine whether they are fit for use. Ascertains the quality of your code. Trains you to write code in a clean and concise way. Time consuming

Convention for unittest is putting test_ or _test at the front or end. 


A Class is like an object constructor, or a "blueprint" for creating objects.
class MyClass:
  x = 5

All classes have a function called __init__(), which is always executed when the class is being initiated. Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

x = 1
print(type("hello")) # <class 'str'>
print(type("x")) # <class 'int'>

def hello():
    print("hello") # <class 'function'>

x = 1
y = "hello"
print (x + y) #TypeError: unsupported oper and type(s) for +: 'int' and 'str'

x = 1
y = 2
x + y 

string = "hello"
print(string.upper()) #HELLO 

class Dog: 
      def__()

A method is a function inside a class. Objects can also contain methods. Methods in objects are functions that belong to the object.The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class. It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()


* Python Inheritance 

Inheritance allows us to define a class that inherits all the methods and properties from another class. Parent class is the class being inherited from, also called base class. Child class is the class that inherits from another class, also called derived class.

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

  #Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class: Use the pass keyword when you do not want to add any other properties or methods to the class.

class Student(Person):
  pass

  class Student(Person):
  def __init__(self, fname, lname):
    #add properties etc.
The child's __init__() function overrides the inheritance of the parent's __init__() function.

Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
class Student(Person): By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

An iterator is an object that contains a countable number of values. An iterator is an object that can be iterated upon, meaning that you can traverse through all the values. Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().

Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.

All these objects have a iter() method which is used to get an iterator:
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.

As you have learned in the Python Classes/Objects chapter, all classes have a function called __init__(), which allows you to do some initializing when the object is being created.

The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.

The __next__() method also allows you to do operations, and must return the next item in the sequence.

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

To prevent the iteration to go on forever, we can use the StopIteration statement. In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times:
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)

Link:
https://www.w3schools.com/python/ Notes made using this website

# Test-Driven Development 

Test-Driven Development - TDD is a software development practice that focuses on coding, testing (unit testing) and refactoring.

Unit testing is a software testing method by which individual units of source code are put under various tests to determine whether they are fit for use. Ascertains the quality of your code. Trains you to write code in a clean and concise way. Time consuming
Very quick, clean and cheap. 

Examples of TDD:
- Write the smallest possible test case that matches what we need to program. 
- Run the test and watch it fail. This gets you into thinking how to write only the code that makes it pass. 
- Write some code with the goal of making the test pass. 
- Run your test suite. Repeat steps 3 and 4 until all tests pass. 
- Go back and refactor your new code, making it as simple and clear as possible while keeping the test suite green. 

/var/folders/nw/pt2fsmrd0gz6dn3q7j7z7_h00000gn/T/TemporaryItems/NSIRD_screencaptureui_zbb1iT/Screenshot\ 2022-05-25\ at\ 10.35.09.png 

Files 
/Users/sharmakenaaleeye/Desktop/Screenshot\ 2022-05-25\ at\ 12.14.31.png 
