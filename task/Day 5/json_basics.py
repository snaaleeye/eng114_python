#JSON - data can only be text - JSON follows pari=ticular rules -
# When we get to data formatting we know how it communicates and how it should look like.
# We know exactly how to manipulate it.
# Another form of data formatting.
# Syntax = from javascript object notation.
# Data = "name": "value"
# {""} Curly brackets hold objects
# {"Name_1:"Value_1". "Name_2"}Data seperated by commas
# Square brackets hold array
#Arrays objects boolean
# JSON dumps dict into strings.
# JSON dump takes two arguments (e.g. dict) and transforms it into JSON

import json

car_data = {"name": "tesla", "engine": "electric"}

with open("new_json_file.json") as jsonfile:
    car = json.load(jsonfile)
    print(type(car))
    print(car['name'])
    print(car['engine'])


# with open('new_json_file.json', 'w') as jsonfile:
#     json.dump(car_data, jsonfile)
# print(type(car_data))
# car_data_json_string = json.dumps(car_data)
# print(car_data_json_string)
# print(type(car_data_json_string))

