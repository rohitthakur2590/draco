

class Solution(object):
    def isBadVersion(self, num):
        return num >= 3

    def firstBadVersion(self, n):
        """
        TC = O(logN)
        :type n: int
        :rtype: int
        A = [3]
        """
        l = 1
        r = n

        while l < r :
            mid = (l + r) // 2
            if self.isBadVersion(mid):
                r = mid
            else:
                l = mid+1
        return l

sol = Solution()

print(sol.firstBadVersion(4))