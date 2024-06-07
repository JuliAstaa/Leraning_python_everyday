""" 
Given an integer array nums, return all the tripple num[i], num[j], num[k] such that i != j, j != k, and num[i] + num[j] + num[k] === 0

Notice the solution set must not contain duplicate triplets

Example:
input: num = [-1, 0, 1, 2, -1, -4]
output: [[-1, -1, 2], [-1, 0, 1]]
explanation:
num[0] + num[1] + num[2] = (-1) + 0 + 1 = 0
num[1] + num[2] + num[4] = 0 + 1 + (-1) = 0
num[0] + num[3] + num[4] = (-1) + 2 + (-1) = 0
The distinct triplets are [-1, 0, 1] and [-1, -1, 2]

Notice that the order of the output and the order of the triplets does not matter
"""

def threeSum(nums: list[int]) -> list[list[int]]:
    h = {} #num : index
    n = len(nums) # panjang array nums
    s = set() # set untuk menyimpan tuples unik

    #loop untuk mengisi dictionary dengan nilai dan indeksnya
    for i, num in enumerate(nums):
        h[num] = i
    
    #loop untuk mencari triplets
    for i in range(n):
        for ii in range(i+1, n):
            #nilai yang dicari agar jumlahnya menjadi nol
            desired = -nums[i] - nums[ii]

            #cek apakah nilai yang dicari ada dalam dictionary dan indeksnya berbeda
            if desired in h and h[desired] != i and h[desired] != ii:
                s.add(tuple(sorted([nums[i], nums[ii], desired]))) # tambahkan triplet dalam bentuk tuple ke set
    
    return s #kembalikan set triplet unik

print(threeSum([-1, 0, 1, 2, -1, -4]))