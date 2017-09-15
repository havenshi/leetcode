# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # iteration
        dummy = ListNode(0)
        while head:
            tmp = head.next
            head.next = dummy.next
            dummy.next = head
            head = tmp
        return dummy.next

        # recursion
    #     return self.helper(head, None)
    #
    # def helper(self, head, newhead):
    #     if head == None:
    #         return newhead
    #     tmp = head.next
    #     head.next = newhead
    #     return self.helper(tmp, head)