# -*- coding:utf8 -*-
"""
url:https://leetcode.com/problems/first-missing-positive/
run time:48 ms(bad), 
tips:

"""


class Solution(object):
    def firstMissingPositive_bad(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        时空复杂度都没有达到O(n)的不良解法
        """
        # 过滤掉非正数，并找到最大最小值
        positive_nums = [n for n in nums if n > 0]
        
        if len(positive_nums) == 0:
            return 1

        # 排序  
        positive_nums.sort()

        if positive_nums[0] > 1:
            return 1

        pre_n = None
        for i, n in enumerate(positive_nums):
            if i == 0:
                pre_n = n
                continue
            elif n == pre_n + 1:
                pre_n = n

        return pre_n + 1

    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 统计正数数量，并找到最大最小值
        positive_count = 0
        max_n = 0
        min_n = 0
        for n in nums:
            if n < 0:
                continue
            positive_count += 1
            if n < min_n:
                min_n = n
            elif n > max_n:
                max_n = n
        
        # 若没有正数，或最小正数大于1，则返回1
        if positive_count == 0 or min_n > 1:
            return 1

        #
        # *暂不考虑有重复数字*
        #
        # 若所有正数都是连续的，则返回最大正数+1
        if positive_count == max_n:
            return max_n + 1

        # TODO
        # 奇数计数/偶数计数是否有用？

        


def test():
    s = Solution()
    test_cases = [
        ([1, 2, 0], 3),
        ([3, 4, 1, -1], 2),
        ([2], 1)
    ]
    for nums, miss_num in test_cases:
        if s.firstMissingPositive(nums) != miss_num:
            print 'Wrong answer in nums:', nums


if __name__ == '__main__':
    test()
