# -*- coding:utf8 -*-
"""
url:https://leetcode.com/problems/valid-anagram/
run time:104 ms
tips:判断组成s和t的字符集是否相等（即每个字母出现的次数相同）
"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        from collections import Counter

        s_counter = Counter(s)
        t_counter = Counter(t)
        if s_counter.viewitems() == t_counter.viewitems():
            return True
        return False
       
        

def test():
    s = Solution()
    string = 'abcdefg'
    print s.isAnagram(string, string[::-1])

if __name__ == '__main__':
    test()
