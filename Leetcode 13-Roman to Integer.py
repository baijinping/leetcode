# -*- coding:utf8 -*-
"""
url:https://leetcode.com/problems/roman-to-integer/
run time:0 ms
tips:
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

        # 前一个字符
        pre_c = None

        # 前一个值
        pre_v = None

        # 实际操作
        oper = operator.add

        # 连续的相同字符之和
        section_sum = 0

        # 遍历计算
        for c in s:
            now_v = roman_value[c]

            # 首个字符
            if not pre_c:
                section_sum = now_v
            else:
                # 遇到相同字符，则继续
                if pre_v == now_v:
                    section_sum += now_v

                else:
                    # 遇到不同字符，根据前后大小关系，改变计算方法
                    if pre_v < now_v:
                        oper = operator.sub
                    elif pre_v > now_v:
                        oper = operator.add

                    result += oper(now_v, section_sum)
                    section_sum = 0

            pre_c = c
            pre_v = now_v

        result += section_sum

        return result

       
        

def test():
    s = Solution()
    roman_num = 'IIIVVVIII'
    print s.romanToInt(roman_num)

if __name__ == '__main__':
    test()
