def unique_in_order(iterables):
    results = []
    for index in range(len(iterables)):
        print(index)
        if iterables[index] != iterables[index - 1]:
            results.append(iterables[index])

print(unique_in_order("AAABBBCCCDDDEEEDDDSSCC"))
