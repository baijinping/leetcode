# -*- coding:utf8 -*-
"""
url:https://leetcode.com/problems/bulb-switcher/
run time:44 ms
tips:逐个计算结果，可以发现规律

n取值 = 0, 1, 4, 9, 16, 25, 36...
结果 = 0, 1, 2, 3, 4, 5, 6, ...
当n=[9, 16)时，结果为3。以此类推
"""


class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        return int(math.sqrt(n))
    
    def bs2(self, n):
        s = 1
        c = 1
        while 1:
            dc = c * c
            if n < dc:
                return c - 1
            s += dc
            c += 1

    def bs3(self, n):
        if n < 1: return 0
        if n is 1: return 1

        switchs = [1] * n
        for i in range(2, n + 1):
            t = i
            while t <= n:
                v = switchs[t - 1]
                switchs[t - 1] = 0 if v is 1 else 1
                t += i

        return switchs.count(1)


def test():
    solution = Solution()

    max_n = 100
    rst_list = []
    for n in range(max_n):
        print n, solution.bulbSwitch(n), solution.bs2(n), solution.bs3(n)
        # rst_list.append(solution.bulbSwitch(n))
    # from collections import Counter
    # counter = Counter(rst_list)
    # print counter
    # print solution.bs(0)
    pass

if __name__ == '__main__':
    test()
    pass
