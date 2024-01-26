"""
Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
"""

my_tuple = (1, 'apple', True, 3.14)
my_list = list(my_tuple) #convert to list
my_list.insert(2, 'banana') # update list, all list method work
my_tuple = tuple(my_list) # convert list to tuples
print(my_tuple) #output: (1, 'orange', True, 3.14)