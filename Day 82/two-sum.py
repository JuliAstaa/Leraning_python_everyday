def two_sum(nums, target):
    checked = {}
    for i, num in enumerate(nums):
        complement = target - num

        if complement in checked:
            return (checked[complement], i)
        
        checked[num] = 1