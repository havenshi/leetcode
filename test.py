# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if n == 0:
            return head
        tmp = head
        count = 0
        while count < n:
            tmp = tmp.next
            count += 1
        tmp2 = head
        while tmp:
            tmp = tmp.next
            tmp2 = tmp2.next
        if tmp2.next != None:
            tmp2.val = tmp2.next.val
            tmp2.next = tmp2.next.next
        else:
            tmp2 = None

        while head:
            print head.val
            head = head.next

if __name__ == '__main__':
    head = ListNode(1)
    tmp = head
    tmp.next = ListNode(2)
    tmp = tmp.next
    tmp.next = ListNode(3)
    tmp = tmp.next
    tmp.next = ListNode(4)
    tmp = tmp.next
    tmp.next = ListNode(5)

    Solution().removeNthFromEnd(head, 1)
