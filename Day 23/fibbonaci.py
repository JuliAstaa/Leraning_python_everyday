def fibonaci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)

    return fib_sequence[:n]

print(fibonaci(10))