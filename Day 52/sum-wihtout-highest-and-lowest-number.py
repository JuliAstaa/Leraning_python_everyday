def sum_array(arr):
    return 0 if arr == None else sum(sorted(arr)[1:-1])
   

print(sum_array(list([6, 2, 1, 8, 10])))



