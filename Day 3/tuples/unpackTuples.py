#unpacking tuples
# ex:
cars = ('Toyota', 'Honda', 'Nissan', 'BMW', 'Ford')

(Toyota, Honda, Nissan, BMW, Ford) = cars
print(Toyota) #output Toyota
print(Honda) #output Honda
print(Nissan) #output Nissan
print(BMW) #output BMW
print(Ford) #output Ford

# use asterisk*
cars = ('Toyota', 'Honda', 'Nissan', 'BMW', 'Ford')
(toyota, honda, *cars) = cars
print(Toyota) #output Toyota
print(Honda) #output Honda
print(*cars) #output Nissan BMW Ford