# -*- coding:utf8 -*-
"""
url:https://leetcode.com/problems/single-number-iii/
run time:60 ms
"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        counter = Counter(nums)
        return [k for k, v in counter.iteritems() if v == 1]


def test():
    s = Solution()
    print s.singleNumber(range(10) * 10 + [9999, 10000])
    pass

if __name__ == '__main__':
    test()
