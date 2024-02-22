def high(str):
    return max(str.split(), key = lambda word: sum(ord(char) - 96 for char in word))

print(high("aku pergi ke pasar"))