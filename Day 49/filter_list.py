def filter_list(l):
    return [x for x in l if isinstance(x, (int, float))]

print(filter_list([1, 2, "a", "b", 3.5, "c"]))