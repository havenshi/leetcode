# Given a non-negative number represented as a singly linked list of digits, plus one to the number.
#
# The digits are stored such that the most significant digit is at the head of the list.
#
# Example:
# Input:
# 1->2->3
#
# Output:
# 1->2->4

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        lst = []
        cur = head

        while cur:
            lst.append(cur)
            cur = cur.next

        carry = 1
        for i in range(len(lst) - 1, -1, -1):
            lst[i].val += carry
            if lst[i].val < 10:
                carry = 0
                break
            else:
                lst[i].val -= 10

        if carry == 1:
            node = ListNode(1)
            node.next = head
            return node
        else:
            return head