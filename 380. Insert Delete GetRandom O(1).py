# Time:  O(1)
# Space: O(n)

import random


class RandomizedSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dictionary = {}
        self.array = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dictionary:
            return False
        self.dictionary[val] = len(self.array)
        self.array.append(val)
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if not val in self.dictionary:
            return False
        # 将末尾的元素换到对应的remove位置上
        index = self.dictionary[val]
        if index == len(self.array) - 1:
            self.array.pop()
            del self.dictionary[val]
            return True
        else:
            tail = self.array.pop()
            self.array[index] = tail
            self.dictionary[tail] = index
            del self.dictionary[val]
            return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.array[random.randint(0, len(self.array) - 1)]


        # Your RandomizedSet object will be instantiated and called as such:
        # obj = RandomizedSet()
        # param_1 = obj.insert(val)
        # param_2 = obj.remove(val)
        # param_3 = obj.getRandom()