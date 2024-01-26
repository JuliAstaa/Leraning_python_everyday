"""
loop in python can using for loop, while, and list comprehension
ex:
"""

games = ['Minecraft', 'Teraria', 'Harvest Moon']
print('for loop\b')
for game in games:
    print(game)
print('\b')

# loop throung the index number, use range() and len() mtehod to create a suitable iterable
print('loop throung the index number\b')
for game in range(len(games)):
    print(games[game])
print('\b')

# while loop
print('while loop\b')
i = 0
while i < len(games):
    print(games[i])
    i += 1
print('\b')

# list  comprehension
print('list comprehension\b')
[print(game) for game in games]
print('\b')