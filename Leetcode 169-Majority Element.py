# -*- coding:utf8 -*-
"""
url:https://leetcode.com/problems/majority-element/
run time:68 ms
tips:昨天刚看到Counter，今天刚好就用了
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        counter = Counter(nums)
        return counter.most_common(1)[0][0]
        

def test():
    s = Solution()
    print s.majorityElement(range(10) + [0] * 10)
    pass

if __name__ == '__main__':
    test()
