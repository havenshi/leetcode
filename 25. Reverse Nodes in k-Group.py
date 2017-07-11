# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return
        dummy = ListNode(0)
        dummy.next = head
        start = dummy
        while start.next:
            end = start
            for i in range(k - 1):
                end = end.next
                if not end.next:
                    return dummy.next  # no k-group
            res = self.reverse(start.next, end.next)
            start.next = res[0]  # new start = original end
            start = res[1]  # start from new end = original start
        return dummy.next

    def reverse(self, start, end):
        head = ListNode(0)
        head.next = start
        while head.next != end:  # exchange start and start.next several times. cannot use 'start.next', since there might be nodes after start.
            tmp = start.next
            start.next = tmp.next
            tmp.next = head.next
            head.next = tmp
        return [end, start]
