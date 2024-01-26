# join list in python like concatination use operator +

flowers = ['rose', 'jasmine', 'orchid', 'lotus', 'cherry blossom', 'dahlia']
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

natures = flowers + fruits
print(natures) #output: ['rose', 'jasmine', 'orchid', 'lotus', 'cherry blossom', 'dahlia', 'apple', 'banana', 'cherry', 'kiwi', 'mango']

#another way join two list, by appending one by one
#ex:
mobile_phones = ['apple', 'Samsung', 'huawei', 'Xiaomi']
mobile_phones2 = ['onePlus', 'Google Pixel', 'LG', 'Sony', 'motorola']

for phone in mobile_phones:
    mobile_phones2.append(phone)

print(mobile_phones2) #output: ['onePlus', 'Google Pixel', 'LG', 'Sony', 'motorola', 'apple', 'Samsung', 'huawei', 'Xiaomi']

#or you can use extend() mtehod, where the purpose is to add elements from one list to another list
# ex:
cars1 = ['Toyota', 'Honda', 'Nissan', 'BMW', 'Ford']
cars2 = ['Mercedes-Benz', 'Audi', 'Chevrolet', 'Volkswagen', 'Hyundai']

cars1.extend(cars2)
print(cars1) #output: ['Toyota', 'Honda', 'Nissan', 'BMW', 'Ford', 'Mercedes-Benz', 'Audi', 'Chevrolet', 'Volkswagen', 'Hyundai']