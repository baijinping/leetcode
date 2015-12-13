# -*- coding:utf8 -*-
"""
url:https://leetcode.com/problems/n-queens/
run time:204 ms(recursioon), 272 ms(un_recursion)
tips:用递归进行回溯,对无效的路径剪枝
"""


class Solution(object):
    # 解答过程中判断是否冲突的次数
    check_valid_count = 0

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
        self.check_valid_count += 1

        for sx, sy in stack:
            if self.check_is_conflict(sx, sy, x, y):
                return False
        return True

    def solve_n_queens_recursion(self, n):
        """
        n皇后问题的递归解法
        """
        if n == 1:
            return [['Q']]
        elif n < 4:
            return []

        solutions = []
        self._find_solution(n, [], solutions)
        return solutions

    def _find_solution(self, n, stack, solutions, col=1):
        """
        n皇后问题的递归主体
        """
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

    def solve_n_queens_un_recursion(self, n):
        """
        n皇后问题的非递归解法
        """
        if n == 1:
            return [['Q']]
        elif n < 4:
            return []

        solutions = []

        stack = [(1, 1)]
        while len(stack) != 0:
            lx, ly = stack.pop(-1)

            # 当前是有效点，向右找
            if self.check_is_valid_pos(stack, lx, ly):
                stack.append((lx, ly))
                if lx < n:
                    stack.append((lx + 1, 1))
                    continue
                else:
                    solution = self.gener_solution_with_stack(n, stack)
                    solutions.append(solution)

            # 当前不是有效点,向下找
            if ly < n:
                stack.append((lx, ly + 1))
            # 当前列已经查找完毕
            elif ly == n:
                # 回溯
                while len(stack) > 0:
                    px, py = stack.pop(-1)
                    if py < n:
                        stack.append((px, py + 1))
                        break

        return solutions


def test():
    s = Solution()
    import time
    for n in range(4, 10):
        print n, '-' * 30

        st = time.time()
        solutions = s.solve_n_queens_un_recursion(n)
        et = time.time()
        print len(solutions), et - st, s.check_valid_count

        s.check_valid_count = 0
        st2 = time.time()
        solutions = s.solve_n_queens_recursion(n)
        et = time.time()
        print len(solutions), et - st2, s.check_valid_count


if __name__ == '__main__':
    test()
