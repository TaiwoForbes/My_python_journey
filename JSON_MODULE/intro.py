import json
import string

# Encoding a data into  json
d = {
    'foo': 'bar',
    'alice': 1,
    'wonderland': [1, 2, 3]
}

with open("json.txt", 'w') as f:
    json.dump(d, f)

# Retrieving data from a file

'''with open("json.txt" , "r") as f:
    d = json.load(f)
    print(d)'''


# Formatting JSON output
data = {"cats": [{"name": "Tubbs", "color": "white"},
                 {"name": "Pepper", "color": "black"}]}
# setting indentation to make the output looks prettier
'''print(json.dumps(data, indent=5))'''


# sorting key alphabetically to get more precise output
print(json.dumps(data, sort_keys=True))

# Getting ride of whitespace
print(json.dumps(data, separators=(",",':') )) # Note : separators make use of two arguments


# Usibg the file base function
from io import StringIO

json_file = StringIO()
date =  {u"foo": u"bar", u"baz": []}
json.dump(data, json_file)
json_file.seek(0)
json_file.content = json_file.read()
json_file.seek(0)
print(json.load(json_file))