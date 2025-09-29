# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 0, n
        res = -1

        while l <= r:

            m = l + (r - l) // 2

            if isBadVersion(m):
                res = m
                r = m - 1
            else:
                l = m + 1

        return res