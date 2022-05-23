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