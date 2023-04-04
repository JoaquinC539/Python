users = ["Dave", "John", "Peter"]

data = ['Dave', 42, True]

emptyList = []

print("Dave" in data)
print(users[0])
print(users[-2])

print(users.index("John"))

print(users[0:2])
print(users[1:])
print(users[-3:-1])
print(len(data))
users.append("Sara")
print(users)
users += ['Jason']
print(users)
users.extend(["Robert", "Jimmy"])
print(users)

# users.extend(data)
# print(users)

users.insert(0, "Bob")
print(users)
users[2:2] = ["Kevin", "Alex"]
print(users)
users.remove("Bob")
print(users)
print(users.pop())
print(users)
del users[0]
print(users)
users[1:2] = ['dave']
users.sort()
print(users)


myList = list([1, "Neil", True])
print(myList)

##### Tuples###############

mytuple = tuple(("Dave", 42, True))
anothertuple = (1, 4, 6, 3, 4)
print(mytuple)
print(type(mytuple))

newList = list(mytuple)
newList.append("Neil")
newtuple = tuple(newList)
print(newtuple)
print(anothertuple.count(4))
