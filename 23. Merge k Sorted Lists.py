# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # method 1 divide and conquer
        # 假设总共有k个list，每个list的最大长度是n，那么运行时间满足递推式T(k) = 2T(k/2)+O(n*k)。
        # 根据主定理，可以算出算法的总复杂度是O(nklogk)
        # 空间复杂度的话是递归栈的大小O(logk)
        if len(lists) <= 1:
            return lists[0] if len(lists) == 1 else None
        elif len(lists) == 2:
            return self.mergeTwoLists(lists[0], lists[1])
        else:
            mid = len(lists) / 2
            left = self.mergeKLists(lists[:mid])
            right = self.mergeKLists(lists[mid:])
            return self.mergeTwoLists(left, right)

    def mergeTwoLists(self, l1, l2):
        res = ListNode(0)
        tmp = res
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next
        if l1 != None:
            tmp.next = l1
        else:
            tmp.next = l2
        return res.next

        # method 2
        # time: nO(k)
        # 维护一个大小为k的堆，每次取堆顶的最小元素放到结果中， 然后读取该元素的下一个元素放入堆中，重新维护好。
        # 因为每个链表是有序的，每次又是去当前k个元素中最小的，所以当所有链表都读完时结束，这个时候所有元 素按从小到大放在结果链表中。
        # 这个算法每个元素要读取一次，即是k*n次，然后每次读取元素要把新元素插入堆中要logk的复杂度，所以总时间复杂度是 O(nklogk)。
        # 空间复杂度是堆的大小，即为O(k)。
        heap = []
        for node in lists:
            if node:
                heap.append((node.val, node))
        heapq.heapify(heap) #压入堆中,Transform list heap into a heap, in-place, in linear time.
        dummy = ListNode(0)
        curr = dummy
        while heap:
            pop = heapq.heappop(heap) #从h中删除最小的(linear时间)，并返回该值
            curr.next = ListNode(pop[0])
            curr = curr.next
            if pop[1].next: #被删除的node
                heapq.heappush(heap, (pop[1].next.val, pop[1].next)) #向堆中增加该node的next
        return dummy.next

        # LTE
        # n = len(lists)
        # flag = [0] * n
        # for i in range(n):
        #     if lists[i]:
        #         flag[i] = 1
        # head = ListNode(0)
        # tmp = head
        # while sum(flag) != 0:
        #     index = 0
        #     while flag[index] == 0:
        #         index += 1
        #     value = lists[index].val
        #     min_index = index
        #     for i in range(index+1, n):
        #         if flag[i] != 0:
        #             if lists[i].val < value:
        #                 min_index = i
        #                 value = lists[min_index].val
        #     tmp.next = lists[min_index]
        #     tmp = tmp.next
        #     lists[min_index] = lists[min_index].next
        #     if not lists[min_index]:
        #         flag[min_index] = 0
        # return head.next

l1= ListNode(1)
l1.next=ListNode(4)
l1.next.next=ListNode(7)
l1.next.next.next=ListNode(10)
l2= ListNode(2)
l2.next=ListNode(5)
l2.next.next=ListNode(8)
l2.next.next.next=ListNode(11)
l3= ListNode(3)
l3.next=ListNode(6)
l3.next.next=ListNode(9)
l3.next.next.next=ListNode(12)
print mergeKLists([l1,l2,l3])