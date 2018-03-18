# Time:  O(n)
# Space: O(1)
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
        dummy = ListNode(0)
        dummy.next = head
        start, end = dummy, dummy
        while start:
            for i in range(k):
                end = end.next
                if not end:
                    return dummy.next
            new_head = start
            new_start = new_head.next
            self.helper(new_head, new_start, end)  # change start and end

            for i in range(k):  # move start to k steps
                start = start.next
            end = start
        return dummy.next

    def helper(self, head, start,
               end):  # 0,1,2,3, exchange 1 and 2 then put 2 to front; exchange 2 and 3 then put 3 to front
        while head.next != end:
            mid = start.next
            start.next = mid.next
            mid.next = head.next
            head.next = mid