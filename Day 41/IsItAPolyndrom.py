def isPolyndrom(str):
    str = str.lower()
    return True if str == str[::-1] else False

print(isPolyndrom("madam"))