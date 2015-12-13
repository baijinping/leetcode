# -*- coding:utf8 -*-
"""
url:https://leetcode.com/problems/reverse-linked-list/
run time:64 ms(recursioon), 60 ms(un_recursion)
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        迭代算法
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        pre_node = None
        cur_node = head

        while cur_node:
            if pre_node is None:
                pre_node = cur_node
                cur_node = pre_node.next
                pre_node.next = None
                continue
            else:
                next_node = cur_node.next
                cur_node.next = pre_node
                pre_node = cur_node
                cur_node = next_node

        return pre_node

    def reverseListRecursion(self, head):
        """
        递归算法
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        return self._reverse_list(head)

    def _reverse_list(self, cur, pre=None):
        """
        递归主体
        """
        if cur is None:
            return pre

        if pre is None:
            next = cur.next
            cur.next = None
            return self._reverse_list(next, cur)
        else:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
            return self._reverse_list(cur, pre)

def show_link_list(head):
    l = []
    while head:
        l.append(str(head.val))
        head = head.next
    print ' '.join(l)


def test():
    s = Solution()
    head = ListNode(0)
    node1 = ListNode(1)
    node2 = ListNode(2)
    head.next = node1
    node1.next = node2

    show_link_list(head)
    new_head = s.reverseListRecursion(head)
    show_link_list(new_head)

if __name__ == '__main__':
    test()
