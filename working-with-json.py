"""
JSON is a syntax for storing and exchanging data.
Python has a built-in package called json, which can be used to work with
JSON data.

Convert from JSON String to Python Object:
If you have a JSON string, you can parse it by using the json.loads() method.
The result will be a python dictionary.

Convert from Python Object to JSON String:
If you have a Python object, you can convert it into a JSON string by using
the json.dumps() method.

"""
print("-------------Example 1-------------------")
import json
import pprint

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y)
print(y["age"])

print("-------------Example 2-------------------")
# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

