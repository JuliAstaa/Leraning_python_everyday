def delete_nth(order,max_e):
    results = []
    for num in order:
        if results.count(num) <= max_e: results.append(num)
    return results
    
print(delete_nth([1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1], 3))