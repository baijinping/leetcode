# -*- coding:utf8 -*-
"""
url:https://leetcode.com/problems/missing-number/
run time:52 ms
tips:
1.由于输入数组是无序的，因此遍历到最后一个数字之前，都不能确定到底是那个数字丢失，因此遍历不可避免
2.一个完整的自然数列和有一个缺失值的自然数列区别就是，其总和不同。差值就是丢失的这个数字
"""
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 无缺失值的数组元素总和
        full_num_sum = int(0.5 * len(nums) * (len(nums) + 1))
        # 当前数组元素总和
        num_sum = sum(nums)

        return full_num_sum - num_sum
        

def test():
    import random
    s = Solution()
    for i in range(10):
        nums = range(100)
        miss_num = random.randint(0, len(nums))
        nums.remove(miss_num)
        random.shuffle(nums)
        print '=' * 30, 'test%d' % i, '=' * 30
        print 'miss num is %d' % miss_num
        print 'find mis num is', s.missingNumber(nums)

if __name__ == '__main__':
    test()
