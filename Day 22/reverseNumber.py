def reverseNumber(num):
    num = num.split(' ')
    num.sort(reverse=True, key=int)
    return " ".join(num)
    

print(reverseNumber("1 2 3 4 5 6 7 8 9 10"))