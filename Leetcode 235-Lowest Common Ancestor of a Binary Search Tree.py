# -*- coding:utf8 -*-
"""
url:https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
run time:152 ms
tip:区分好每个不同角色节点的判断逻辑就行了
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#     def __str__(self):
#         return str(self.val)

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        _, node = self.find_ancestor(root, p, q)
        return node


    def find_ancestor(self, root, p, q):
        if not root:
            return 0, None

        node = root
        
        weight = 0
        # 左边有没有
        if root.left:
            find_num, node = self.find_ancestor(root.left, p, q)
            # 找到了目标，直接返回
            if find_num == 2:
                return 2, node

            # 找到p或q
            if find_num:
                weight += 1

        # 右边有没有
        if root.right:
            find_num, node = self.find_ancestor(root.right, p, q)
            # 找到了目标，直接返回
            if find_num == 2:
                return 2, node

            # 找到p或q
            if find_num:
                weight += 1

        # 自己就是p或q
        if root is p or root is q:
            weight += 1

        # 自己就是目标
        if weight == 2:
            return 2, root

        # 返回查询结果
        else:
            return weight, node

def test():
    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None

        def __str__(self):
            return str(self.val)

    # create test data
    """
            _______6______
           /                           \
        ___2__               ___8__
       /           \         /               \
       0           4       7                  9
                  /   \
                 3     5
    """
    root = TreeNode(6)
    node1 = TreeNode(2)
    node2 = TreeNode(8)
    node3 = TreeNode(0)
    node4 = TreeNode(4)
    node5 = TreeNode(3)
    node6 = TreeNode(5)
    node7 = TreeNode(7)
    node8 = TreeNode(9)

    root.left = node1
    root.right = node2

    node1.left = node3
    node1.right = node4

    node4.left = node5
    node4.right = node6

    node2.left = node7
    node2.right = node8

    s = Solution()
    print s.lowestCommonAncestor(root, node1, node2)

if __name__ == '__main__':
    test()
