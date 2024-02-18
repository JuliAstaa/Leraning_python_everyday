def fizzBuzz(number):
    results = []
    for num in range(1, number + 1):
        if(num % 15 == 0):
            results.append("FizzBuzz")
        elif(num % 3 == 0):
            results.append("Fizz")
        elif(num % 5 == 0):
            results.append("Buzz")
        else: results.append(num)
    return results

print(fizzBuzz(50))
