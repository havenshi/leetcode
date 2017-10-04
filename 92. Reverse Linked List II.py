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
        if m == n:
            return head
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        head1 = dummy
        for i in range(m - 1):
            head1 = head1.next
        p = head1.next  # p == 2
        for i in range(n - m):  # transform 2 times: 12345 > 13245 > 14325, gradually put the node after 2 in front of the right of head1, (n-m) times
            tmp = head1.next
            head1.next = p.next  # add node after m
            p.next = p.next.next
            head1.next.next = tmp
        return dummy.next

        # method 2!!!
        # def reverseKGroup(self, head, k):
        #     """
        #     :type head: ListNode
        #     :type k: int
        #     :rtype: ListNode
        #     """
        #     dummy = ListNode(0)
        #     dummy.next = head
        #     start, end = dummy, dummy
        #     while start:
        #         for i in range(k):
        #             end = end.next
        #             if not end: return dummy.next
        #         self.helper(start, end, k)
        #         for i in range(k):
        #             start = start.next
        #         end = start
        #     return dummy.next
        #
        # def helper(self, start, end, k):
        #
        #     cur = start.next
        #     tail = end.next
        #     for i in range(k):
        #         tmp = cur.next
        #         cur.next = tail
        #         tail = cur
        #         cur = tmp
        #     start.next.next = cur
        #     start.next = tail
        #

        # method 3
        # if m == n:
        #     return head
        #
        # cons = ListNode(0)
        # cons.next = head
        # cur = cons.next
        # pre = cons
        # count = 0  # cursor to record the position
        # while cur != None:
        #     count += 1
        #     if count == m:  # delete node m
        #         tmp1 = cur.val
        #         cur = cur.next
        #         pre.next = cur
        #         continue
        #     elif count == n:  # change the val of node n
        #         tmp2 = cur.val
        #         cur.val = tmp1
        #     pre = cur
        #     cur = cur.next
        #
        # cur = cons.next
        # pre = cons
        # count = 0
        # while cur != None:
        #     count += 1
        #     if count == m:  # add new node
        #         newnode = ListNode(tmp2)
        #         pre.next = newnode
        #         newnode.next = cur
        #         break
        #     pre = cur
        #     cur = cur.next
        # return cons.next

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
    print Solution().reverseBetween(head, 2, 4)