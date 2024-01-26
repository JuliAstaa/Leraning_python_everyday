# sort() method sort the list alphanumeric ascending by default:
# ex
flowers = ['rose', 'jasmine', 'orchid', 'lotus', 'cherry blossom', 'hibiscus', 'dahlia']
flowers.sort()
print(flowers) #output : ['cherry blossom', 'dahlia', 'hibiscus', 'jasmine', 'lotus', 'orchid', 'rose']

# to sort descending use the keyword argument reverse = true
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits.sort(reverse=True)
print(fruits) # output: ['mango', 'kiwi', 'cherry', 'banana', 'apple']

# sort is casesensitive, resulting in all capital letters being sorted before lower case letters
# ex: 
mobile_phones = ['apple', 'Samsung', 'huawei', 'Xiaomi', 'onePlus', 'Google Pixel', 'LG', 'Sony', 'motorola']
mobile_phones.sort()
#output ['Google Pixel', 'LG', 'Samsung', 'Sony', 'Xiaomi', 'apple', 'huawei', 'motorola', 'onePlus']

# perform case-insensitive, u cane use built in func str.lower 
mobile_phones = ['apple', 'Samsung', 'huawei', 'Xiaomi', 'onePlus', 'Google Pixel', 'LG', 'Sony', 'motorola']
mobile_phones.sort(key =str.lower) #output : ['apple', 'Google Pixel', 'huawei', 'LG', 'motorola', 'onePlus', 'Samsung', 'Sony', 'Xiaomi']

print(abs(50-50))

