# Design a hit counter which counts the number of hits received in the past 5 minutes.
#
# Each function accepts a timestamp parameter (in seconds granularity) and you may assume that calls are being made to the system in chronological order (ie, the timestamp is monotonically increasing). You may assume that the earliest timestamp starts at 1.
#
# It is possible that several hits arrive roughly at the same time.
#
# Example:
# HitCounter counter = new HitCounter();
#
# // hit at timestamp 1.
# counter.hit(1);
#
# // hit at timestamp 2.
# counter.hit(2);
#
# // hit at timestamp 3.
# counter.hit(3);
#
# // get hits at timestamp 4, should return 3.
# counter.getHits(4);
#
# // hit at timestamp 300.
# counter.hit(300);
#
# // get hits at timestamp 300, should return 4.
# counter.getHits(300);
#
# // get hits at timestamp 301, should return 3.
# counter.getHits(301);
# Follow up:
# What if the number of hits per second could be very large? Does your design scale?

# 这道题让我们设计一个点击计数器，能够返回五分钟内的点击数，提示了有可能同一时间内有多次点击。由于操作都是按时间顺序的，
# 下一次的时间戳都会大于等于本次的时间戳，那么最直接的方法就是用一个队列queue，每次点击时都将当前时间戳加入queue中，
# 然后在需要获取点击数时，我们从队列开头开始看，如果开头的时间戳在5分钟以外了，就删掉，直到开头的时间戳在5分钟以内停止，
# 然后返回queue的元素个数即为所求的点击数

# Time:  O(1), amortized
# Space: O(k), k is the count of seconds.

from collections import deque

class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        self.queue.insert(0, timestamp)

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        while self.queue and timestamp - self.queue[-1] >= 300:
            self.queue.pop()
        return len(self.queue)

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)