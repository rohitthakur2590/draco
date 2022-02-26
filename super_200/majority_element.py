from collections import  defaultdict
def majority_element(nums):
    hm = defaultdict(int)

    for num in nums:
        if num in hm and hm[num] == len(nums)//2:
            return num
        hm[num] += 1
    return -1

def majority(nums):
    hm = {}

    for num in nums:
        hm[num] = hm.get(num,0) + 1
    for key in hm:
        if hm[key] > len(nums)//2:
            return key
    return -1



nums = [1,2,3,1,2,2,2]

#print("Majority Element: ", majority_element(nums))
print("Majority Element: ", majority(nums))
