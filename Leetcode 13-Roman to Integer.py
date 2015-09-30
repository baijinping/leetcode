# -*- coding:utf8 -*-
"""
url:https://leetcode.com/problems/roman-to-integer/
run time:156 ms
tips:从前往后遍历罗马数字，如果某个数小于等于前一个数，则把该数加入到结果中；
反之，则在结果中两次减去前一个数，并加上当前这个数
"""
import operator

class Solution(object):

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 罗马数字定义
        roman_value = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        # 计算结果
        result = 0

        # 前一个值
        pre_v = None

        # 遍历计算
        for c in s:
            now_v = roman_value[c]

            # 首个字符
            if not pre_v:
                result = now_v
            else:
                # 根据前后大小关系，改变计算方法
                if pre_v < now_v:
                    result -= pre_v * 2
                    result += now_v
                elif pre_v >= now_v:
                    result += now_v

            pre_v = now_v

        return result


def test():
    s = Solution()
    roman_num = 'DCXXI'
    print s.romanToInt(roman_num)

if __name__ == '__main__':
    test()
