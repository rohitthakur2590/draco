from collections import defaultdict
def is_duplicate_exist(nums):
    """
    Time Complexity: O(N)
    Space Complexity: O(N)
    :param nums:
    :return:
    """
    hm = defaultdict(int)

    for num in nums:
        if num in hm:
            return True
        hm[num] += 1
    return False

def is_duplicate(nums):
    return not (sum(nums) == (sum(set(nums))))


nums = [1,2,3,4]
#nums = [1,2,3,1]
print("Duplicate present: ", is_duplicate_exist(nums))
print("Duplicate present: ", is_duplicate(nums))
