# -*- coding:utf8 -*-
"""
url:https://leetcode.com/problems/reverse-linked-list-ii/
run time:48 ms
tips:因为只是旋转部分链表，所以还需要考虑旋转部分前后的关联关系
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or not head.next or m == n:
            return head

        index = 0

        pre_rev_node = None
        first_rev_node = None

        pre_node = None
        cur_node = head
        next_node = None

        while index < n:
            index += 1
            if index < m:
                pre_rev_node = cur_node
                cur_node = cur_node.next
                continue

            if pre_node is None:
                first_rev_node = cur_node

                pre_node = cur_node
                cur_node = pre_node.next
                continue
            else:
                if index < n:
                    next_node = cur_node.next
                    cur_node.next = pre_node
                    pre_node = cur_node
                    cur_node = next_node
                else:
                    # 最后一个交换点
                    next_node = cur_node.next if cur_node else None

                    # 最后一个交换点不是最后一个点
                    if next_node:
                        cur_node.next = pre_node
                        pre_node = cur_node
                        first_rev_node.next = next_node

                    # 最后一个交换点是最后一个点
                    else:
                        cur_node.next = pre_node
                        pre_node = cur_node
                        first_rev_node.next = None

        if m != 1:
            pre_rev_node.next = pre_node
            return head
        else:
            return pre_node
        

def show_link_list(head):
    l = []
    while head:
        val = str(head.val)
        if val not in l:
            l.append(val)
        else:
            l.append(val)
            break
        head = head.next
    print ' '.join(l)


def test():
    s = Solution()
    head = ListNode(0)
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    head.next = node1
    node1.next = node2
    node2.next = node3

    show_link_list(head)
    new_head = s.reverseBetween(head, 1, 2)
    show_link_list(new_head)

if __name__ == '__main__':
    test()
