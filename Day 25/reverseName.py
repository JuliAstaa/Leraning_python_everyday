def reverseName(name):
    name = name.split(" ")
    reversedName = []
    for word in name:
        reversedName.append(word[::-1])
    return " ".join(reversedName)

print(reverseName("I Made Juli Astawa"))
