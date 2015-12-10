# -*- coding:utf8 -*-
"""
url:https://leetcode.com/problems/nim-game/
run time:44 ms
tips:归纳法
"""

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 > 0

def test():
    s = Solution()
    for n in xrange(1, 10):
        print n, s.canWinNim(n)

if __name__ == '__main__':
    test()
    