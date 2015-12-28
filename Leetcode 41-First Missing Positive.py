# -*- coding:utf8 -*-
"""
url:https://leetcode.com/problems/first-missing-positive/
run time:48 ms(bad), 48 ms(better)
tips:
在这道题卡了很久，想方设法找规律，还是纠结在数组的无序性上
最终还是在http://blog.csdn.net/nanjunxiao/article/details/12973173看了解法
原来就差一步，将参数数组本身当做桶，使得数组正数元素在下一次遍历时保持有序接口即可
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
        len_of_nums = len(nums)
        if len_of_nums == 0:
            return 1

        # 第一次遍历，将正数放到与其值对应的位置上
        n = 0
        for i in xrange(len_of_nums):
            n = nums[i]

            tmp = 0
            while 1:
                if not 0 < n < len_of_nums or n == nums[n - 1]:
                    break

                tmp = nums[n - 1]
                nums[n - 1], nums[i], n = n, tmp, tmp

        # 第二次遍历，找到第一个非正数所在位置，返回即可
        for i, n in enumerate(nums):
            if i + 1 != n or n <= 0:
                return i + 1
        else:
            return n + 1


def test():
    s = Solution()
    test_cases = [
        ([1, 2, 0], 3),
        ([3, 4, 1, -1], 2),
        ([2], 1),
        ([1, 1], 2),
        ([3, 1], 2),
        ([1], 2),
        ([2, 1], 3),
        ([], 1)
    ]
    for nums, miss_num in test_cases:
        if s.firstMissingPositive(nums) != miss_num:
            print 'Wrong answer in nums:', nums


if __name__ == '__main__':
    test()