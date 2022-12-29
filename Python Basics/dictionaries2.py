# the for loop
#for item in (1,2,3,4,5,6,7,8,9):
   # print(item)

user = {
    'name': 'juma',
    'age': 1000,
    'school': 'moi university'
}

for item in user.items():
    print(item)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)

print([i.lower() for i in "Python"])
