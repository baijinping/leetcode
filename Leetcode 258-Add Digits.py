# -*- coding:utf8 -*-
"""
url:https://leetcode.com/problems/add-digits/
run time:76 ms
tip:一般思路的解法是addDigits1，写出来之后尝试找100以内数字和输出的规律，得出解法2
"""

class Solution:
    def addDigits1(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num

        n = num
        while n >= 10:
            # 计算各位和
            sum_digit = 0
            while n > 0:
                t2 = n % 10
                sum_digit += t2
                n /= 10

            # 重新设定n
            n = sum_digit

        return n

    def addDigits2(self, num):
        if num < 10:
            return num

        n = num % 9
        return n if n != 0 else 9

def test():
    s = Solution()
    for i in xrange(100000):
        assert(s.addDigits1(i) == s.addDigits2(i))

    pass

if __name__ == '__main__':
    test()
