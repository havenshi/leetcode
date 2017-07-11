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
        heap = []
        for node in lists:
            if node:
                heap.append((node.val, node))
        heapq.heapify(heap) #压入堆中
        head = ListNode(0); curr = head
        while heap:
            pop = heapq.heappop(heap) #从h中删除最小的(linear时间)，并返回该值
            curr.next = ListNode(pop[0])
            curr = curr.next
            if pop[1].next: #被删除的node
                heapq.heappush(heap, (pop[1].next.val, pop[1].next)) #向堆中增加该node的next
        return head.next

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