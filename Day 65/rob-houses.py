def rob_houses(houses: list[int]) -> int:
    n = len(houses)

    prev = houses[0]
    curr = max(houses[0], houses[1])

    for x in range(2, n):
        prev, curr = curr, max(houses[x] + prev, curr)
    return curr

print(rob_houses([1,2]))