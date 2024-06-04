
#menggunakan metode sum
def finding_the_missing_number_sum(nums: list[int]) -> int:
    n = max(nums)
    expected = n * (n+1) // 2
    return expected

print(finding_the_missing_number_sum([0,1,2,3,5,6,7,8,9]))

#mrnggunakan metode XOR "^"
def finding_the_missing_number_xor(nums: list[int]) -> int:
    n = max(nums)
    expected_xor = 0
    nums_xor = 0

    for num in nums:
        nums_xor ^= num
    
    for x in range(n + 1):
        expected_xor ^= x
    
    return expected_xor ^ nums_xor

print(finding_the_missing_number_xor([1,0,3]))


# mencari lebih dari satu angka, menggunakan metode set()
def finding_missing_numbers(nums: list[int]) -> list[int]:
    n = max(nums)
    all_numbers = set(range(min(nums), n + 1))
    return list(all_numbers - set(nums))
    
print(finding_missing_numbers([1, 2, 4, 6]))  # Output: [3, 5]