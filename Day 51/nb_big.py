def nb_big(n, d):
    sqrt= []
    digitCounted = []
    for x in range (0, n +1):
        sqrt.append(x**2)
    
    for number in sqrt:
        for num in str(number):
            if str(d) in str(num):
                digitCounted.append(number)

    
    print(digitCounted)
    
    return len(digitCounted)

    
  

print(nb_big(11011, 2))


# alternatif, top 1 answer at codewars
def nb_dig(n, d):
    return sum(str(i*i).count(str(d)) for i in range(n+1))
