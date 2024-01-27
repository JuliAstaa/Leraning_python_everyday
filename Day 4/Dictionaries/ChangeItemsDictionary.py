# Change item dictionary
# You can change the value of a specific item by referring to its key name
# ex:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car['year'] = 1970
print(car) #output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1970}

# The update() method will update the dictionary with the items from the given argument. The argument must be a dictionary, or an iterable object with key:value pairs.
# ex:
myFood = {
    'name': 'Nasi Goreng',
    'hot': False,
    'portion': 'large'
}
myFood.update({'hot': True})
print(myFood) #output: {'name': 'Nasi Goreng', 'hot': True, 'portion': 'large'}

