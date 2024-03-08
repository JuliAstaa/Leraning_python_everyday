def number(list: list):
    results = []
    for index in range(len(list)):
        results.append(f"{index + 1}: {list[index]}")
    return results

print(number(["a", "b", "c"]))