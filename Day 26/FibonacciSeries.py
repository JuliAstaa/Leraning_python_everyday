def fibonacci(number):
    fibSequence = [0, 1]

    while len(fibSequence) < number:
        nextFib = fibSequence[-1] + fibSequence[-2]
        fibSequence.append(nextFib)
    
    print(fibSequence[:number])

fibonacci(10)