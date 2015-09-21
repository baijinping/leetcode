# -*- coding:utf8 -*-
"""
url:https://leetcode.com/problems/search-insert-position/
run time:40 ms
tips:水题
"""


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i, n in enumerate(nums):
            if n >= target:
                return i
        return len(nums)
        

def test():
    s = Solution()
    import random
    print s.searchInsert(range(1, 10), random.randint(1, 10))

if __name__ == '__main__':
    test()
