# -*- coding:utf8 -*-
"""
url:https://leetcode.com/problems/contains-duplicate/
run time:56 ms
tip:字典基于哈希表，查找O(1);列表基于链表，查找O(n)
"""
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        appear_num = {}
        for n in nums:
            if n in appear_num:
                return True
            appear_num[n] = 0
            
        return False
        

def test():
    s = Solution()
    print s.containsDuplicate(range(100000))
    pass

if __name__ == '__main__':
    test()
