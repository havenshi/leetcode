# Time:  O(n)
# Space: O(1)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        head = dummy
        carry = 0
        while l1 or l2 or carry:
            value = 0
            if l1:
                value += l1.val
                l1 = l1.next
            if l2:
                value += l2.val
                l2 = l2.next
            value += carry
            head.next = ListNode(value % 10)
            carry = value / 10
            head = head.next

        return dummy.next
if __name__ == "__main__":
    answer = Solution()
    l1 = ListNode(2)
    l12 = ListNode(4)
    l13 = ListNode(3)
    l1.next=l12
    l12.next=l13
    l2 = ListNode(5)
    l22 = ListNode(6)
    l23 = ListNode(4)
    l2.next=l22
    l22.next=l23
    print answer.addTwoNumbers(l1, l2)

