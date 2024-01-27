# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# unchangeable Set items are unchangeable, meaning that we cannot change the items after the set has been created.
# duplicate are not allowed, Sets cannot have two items with the same value.
# ex:
mySet = {"apple", "banana", "cherry", "apple"}
print(mySet) #output: {'cherry', 'apple', 'banana'}

# true and 1 is same value
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset) #output: {True, 2, 'cherry', 'apple', 'banana'}

# as well as False and 0, they are the same value
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset) #output: {False, True, 'cherry', 'apple', 'banana'}

# get length of the set
set_mobil = {"Toyota", "Honda", "Suzuki", "BMW"}
print(len(set_mobil)) #output: 4

# set type
set_mobil = {"Toyota", "Honda", "Suzuki", "BMW"}
print(type(set_mobil)) #output: <class 'set'>

# set constructor
flowersSet = set(('rose', 'jasmine','lotus'))
print(flowersSet) #output: {'lotus', 'rose', 'jasmine'}