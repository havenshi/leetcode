# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # O(n) time, O(n) space
        s1 = self.count(l1)
        s2 = self.count(l2)
        s = max(s1, s2)

        # sum all bits, 7,7,10,7
        dummy = ListNode(0)
        head = dummy
        while s:
            head.next = ListNode(0)
            head = head.next
            if s <= s1:
                head.val += l1.val
                l1 = l1.next
            if s <= s2:
                head.val += l2.val
                l2 = l2.next
            s -= 1

        # if val > 9, from pre to cur, all +1
        p = dummy
        while p:
            q = p.next
            while q and q.val == 9:
                q = q.next
            if q and q.val > 9:
                while p != q:
                    p.val += 1
                    p = p.next
                    p.val -= 10
            else:
                p = q

        if dummy.val == 0:
            return dummy.next
        else:
            return dummy

    def count(self, l):
        count = 0
        while l:
            count += 1
            l = l.next
        return count

    #     l1 = self.reverse(l1)
    #     l2 = self.reverse(l2)
    #
    #     dummy = ListNode(0)
    #     tmp = dummy
    #     carry = 0
    #     while l1 or l2 or carry:
    #         value = 0
    #         if l1:
    #             value += l1.val
    #             l1 = l1.next
    #         if l2:
    #             value += l2.val
    #             l2 = l2.next
    #         if carry:
    #             value += 1
    #         carry = value / 10
    #         value = value % 10
    #         tmp.next = ListNode(value)
    #         tmp = tmp.next
    #     return self.reverse(dummy.next)
    #
    # def reverse(self, head):
    #     dummy = ListNode(0)
    #     while head:
    #         tmp = head.next
    #         head.next = dummy.next
    #         dummy.next = head
    #         head = tmp
    #     return dummy.next