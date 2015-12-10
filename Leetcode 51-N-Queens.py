# -*- coding:utf8 -*-
"""
url:https://leetcode.com/problems/n-queens/
run time:204 ms
tips:用递归进行回溯,对无效的路径剪枝
"""


class Solution(object):
    def gener_solution_with_stack(self, n, stack):
        """
        根据栈中的记录，生成一个有效解答
        """
        solution = []
        for col, row in stack:
            line = '.' * (row - 1) + 'Q' + '.' * (n - row)
            solution.append(line)
        return solution
        

    def check_is_conflict(self, x1, y1, x2, y2):
        """
        检查(x1, y1)和(x2, y2)的位置是否冲突
        """
        # 直线冲突
        if x1 == x2 or y1 == y2:
            return True

        # 斜线冲突
        if abs(x1 - x2) == abs(y1 - y2):
            return True

        return False

    def check_is_valid_pos(self, stack, x, y):
        """
        检查在当前的摆放中，(x, y)是否一个有效的新位置
        """
        for sx, sy in stack:
            if self.check_is_conflict(sx, sy, x, y):
                return False
        return True

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n == 1:
            return [['Q']]
        elif n < 4:
            return []

        solutions = []
        self._find_solution(n, [], solutions)
        return solutions

    def _find_solution(self, n, stack, solutions, col=1):
        if col > n:
            return

        for row in xrange(1, n + 1):
            new_x, new_y = col, row
            if self.check_is_valid_pos(stack, col, row):
                stack.append((col, row))

                # 还没有找到一个完整解法，继续递归
                if len(stack) < n:
                    self._find_solution(n, stack, solutions, col + 1)
                # 找到完整解法，生成返回结果
                else:
                    solution = self.gener_solution_with_stack(n, stack)
                    solutions.append(solution)

                stack.pop(-1)

def test():
    s = Solution()
    s.solveNQueens(8)

if __name__ == '__main__':
    test()
    