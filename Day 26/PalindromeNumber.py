def isPalindrome(number):
    numberStr = str(number)
    return True if numberStr == numberStr[::-1] else False

print(isPalindrome([1,2,3,4,3,2,1]))