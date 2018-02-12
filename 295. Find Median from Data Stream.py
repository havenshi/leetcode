# -*- coding: utf-8 -*-
# 我们使用大小堆来解决问题，其中大堆保存右半段较大的数字，小堆保存左半段较小的数组。这样整个数组就被中间分为两段了，
# 由于堆的保存方式是由大到小，我们希望大堆里面的数据是从小到大，这样取第一个来计算中位数方便。我们用到一个小技巧，
# 就是存到大堆里的数先取反再存，这样由大到小存下来的顺序就是实际上我们想要的从小到大的顺序。

import heapq

class MedianFinder(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.large_h = []
        self.small_h = []
        self.large_size = 0
        self.small_size = 0

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if self.small_size == 0:
            heapq.heappush(self.small_h, -num)
            self.small_size += 1
            return
        elif self.large_size == 0:
            s = -(heapq.heappop(self.small_h))
            if s > num:
                s, num = num, s
            heapq.heappush(self.small_h, -s)
            heapq.heappush(self.large_h, num)
            self.large_size += 1
            return

        l = heapq.heappop(self.large_h)
        s = -(heapq.heappop(self.small_h))
        if self.large_size == self.small_size:
            if num <= s:
                heapq.heappush(self.small_h, -num)
                self.small_size += 1
            else:
                heapq.heappush(self.large_h, num)
                self.large_size += 1

        else:
            if self.large_size > self.small_size:
                if num > l:
                    l, num = num, l
                heapq.heappush(self.small_h, -num)
                self.small_size += 1
            else:
                if num < s:
                    s, num = num, s
                heapq.heappush(self.large_h, num)
                self.large_size += 1

        heapq.heappush(self.large_h, l)
        heapq.heappush(self.small_h, -s)
        heapq.heapify(self.large_h)
        heapq.heapify(self.small_h)

    def findMedian(self):
        """
        :rtype: float
        """
        if self.small_size == 0 and self.large_size == 0:
            return None
        elif self.small_size == 0:
            l = heapq.heappop(self.large_h)
            heapq.heappush(self.large_h, l)
            return l / 1.0
        elif self.large_size == 0:
            s = -(heapq.heappop(self.small_h))
            heapq.heappush(self.small_h, -s)
            return s / 1.0

        l = heapq.heappop(self.large_h)
        s = -(heapq.heappop(self.small_h))
        if self.large_size == self.small_size:
            median = (l + s) / 2.0
        else:
            if self.large_size > self.small_size:
                median = l / 1.0
            else:
                median = s / 1.0

        heapq.heappush(self.large_h, l)
        heapq.heappush(self.small_h, -s)
        heapq.heapify(self.large_h)
        heapq.heapify(self.small_h)

        return median

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
