           # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head: return True

        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        cur = slow.next
        tail = None
        while cur: # 后半段翻转
            tmp = cur.next
            cur.next = tail
            tail = cur
            cur = tmp

        p1, p2 = head, tail
        while p2:
            if p1.val == p2.val:
                p1 = p1.next
                p2 = p2.next
            else:
                return False
        return True

