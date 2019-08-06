# 蓄水池抽样算法的等概率性可以用数学归纳法证明：
#
# I   当链表长度为1时，random.randint(0, 0)恒等于0，因此抽到第1个元素的概率为1
#
# II  假设抽取前n个元素的概率相等，均为1/n
#
# III 当抽取第n+1个元素时：
#
# 若random.randint(0, n)等于0，则返回值替换为第n+1个元素，其概率为1/(n+1)；
#
# 否则，抽取的依然是前n个元素，其概率为1/n * n/(n+1) = 1/(n+1)

import random
class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head. Note that the head is guanranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        res = None
        cnt = 0
        head = self.head
        while head:
            if random.randint(0, cnt) == 0:
                res = head.val
            head = head.next
            cnt += 1
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()