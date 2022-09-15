import json

'''with open("a.txt", "r") as f:
    resd = json.load(f)
    print(resd)'''


d = {
    'foo': 'ba',
    'alice': 1,
    'wonderland': [1, 2, 3]
}

with open("a.txt", "w") as f:
    (json.dump(d,f,indent = 5))
    (json.dump(d,f,indent = 5))
    (json.dump(d,f,indent = 5))
    (json.dump(d,f,indent = 5))
    (json.dump(d,f,indent = 5))    
  