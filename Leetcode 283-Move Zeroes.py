# -*- coding:utf8 -*-
"""
url:https://leetcode.com/problems/move-zeroes/
run time:128 ms
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero_count = nums.count(0)
        for i in xrange(zero_count):
            nums.remove(0)
        for i in xrange(zero_count):
            nums.append(0)
        

def test():
    s = Solution()
    
    l = [2,3,1,0,9,8,0,0,8,7,7,0,0]
    print l
    s.moveZeroes(l)
    print l

if __name__ == '__main__':
    test()
