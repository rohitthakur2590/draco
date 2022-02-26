class Solution(object):
    def missingNumber_brute_force(self, nums):
        """
        TC = 2 * O(N)
        SC = O(1)
        :type nums: List[int]
        :rtype: int
        """

        hm = set()

        for num in nums:
            hm.add(num)
        for i in range(len(nums) + 1):
            if i not in hm:
                return i

    def missingNumber_OPTIMAL(self, nums):
        """
        TC = O(N) + O (1)
        SC = O(1)
        :param nums:
        :return:
        """
        curr_sum = sum(nums)
        n = len(nums)
        son = (n * (n + 1)) / 2
        return son - curr_sum
