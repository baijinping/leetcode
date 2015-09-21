# -*- coding:utf8 -*-
"""
url:https://leetcode.com/problems/product-of-array-except-self/
run time:168 ms
tips:
"""


class Solution(object):
    def productExceptSelfOld(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        len_n = len(nums)
        products = [1] * len_n
        for i, n in enumerate(nums):
            for j, n in enumerate(nums):
                if j != i:
                    products[i] *= nums[j]
        return products


    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []

        len_n = len(nums)

        # 计算结果
        products = [1] * len_n

        # 前面所有元素之积
        pre_product = 1

        # 后面所有元素之积
        post_product = 1

        # 逆序遍历nums,在products中插入后面元素之积
        for i, n in enumerate(reversed(nums)):
            products[len_n - i - 1] = post_product
            post_product *= n

        # 正序遍历nums,在products中乘以前面元素之积
        for i, n in enumerate(nums):
            products[i] *= pre_product
            pre_product *= n

        return products



def test():
    s = Solution()
    print s.productExceptSelf(range(1, 100))
    print s.productExceptSelfOld(range(1, 100))

if __name__ == '__main__':
    test()
