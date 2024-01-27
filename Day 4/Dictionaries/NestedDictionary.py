#Nested Dictionary
# A dictionary can contain dictionaries, this is called nested dictionaries.
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# access nested dictonary
print(myfamily['child1']['name']) #output: Emil

# loop nested dictionary
for child in myfamily:
    for name, value in myfamily[child].items():
        print(child ,name, ': ', value)
"""
output:
child1 name :  Emil
child1 year :  2004
child2 name :  Tobias
child2 year :  2007
child3 name :  Linus
child3 year :  2011
"""