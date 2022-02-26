def brute_force(nums, target):
    """
    TC = 2*O(N) => O(N)
    SC =  O(1)
    A = [10, 11, 11, 11, 17, 18]
    :param A:
    :param ele:
    :return:
    """

    start = -1
    end = -1
    n = len(nums)
    for i in range(n):
        if nums[i] == target:
            start = i
            break
    if start != n and start != -1:
        for j in range(n - 1, start - 1, -1):
            if nums[j] == target:
                end = j
                break
    return [start, end]


class Solution(object):
    """
    TC = 2 * O(LOGN)
    SC = O(1)
    """
    def getLeftPosition(self, nums, target):

        l = 0
        r = len(nums) - 1

        while (l <= r):
            mid = (l + r) // 2

            if nums[mid] == target:
                if mid == 0 or nums[mid - 1] != target:
                    return mid
                r = mid - 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1

    def getRightPosition(self, nums, target):
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                if (mid == (len(nums) - 1)) or (nums[mid + 1] != target):
                    return mid
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = self.getLeftPosition(nums, target)
        right = self.getRightPosition(nums, target)

        return [left, right]

A = [10, 11, 11, 11, 17, 18]
print(brute_force(A, 11))