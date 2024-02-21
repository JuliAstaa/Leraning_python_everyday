def countUniqueChar(str):
    uniqueChar = set()

    for char in str:
        uniqueChar.add(char)

    return len(uniqueChar)

print(countUniqueChar("Hello"))