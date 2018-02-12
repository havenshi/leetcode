# -*- coding: utf-8 -*-
class LRUCache(object):
    # 双向链表，表头表示最近使用过的数据，越接近表尾表示越久没有使用过。
    # 当要将旧数据删除时，我们只需要将链表尾部的节点去除，并在头部插入新的节点。
    # 而更新节点时，我们只需要将原来的节点删除，改变节点的内容，再插入到链表头部。
    # 而最简单的插入，即还没有达到容量上限时，我们只要在头部直接插入。

    class Node(object):
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev, self.next = None, None

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity, self.size = capacity, 0
        self.dic = {}
        self.head, self.tail = self.Node(-1, -1), self.Node(-1, -1)
        self.head.next, self.tail.prev = self.tail, self.head

    def __remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev, node.next = None, None

    def __insert(self, node):
        node.prev, node.next = self.head, self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dic:
            return -1
        node = self.dic[key]
        self.__remove(node)
        self.__insert(node)
        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.dic:
            node = self.dic[key]
            self.__remove(node)
            node.value = value
            self.__insert(node)
        else:
            if self.size == self.capacity:
                discard = self.tail.prev
                self.__remove(discard)
                del self.dic[discard.key]
                self.size -= 1
            node = self.Node(key, value)
            self.dic[key] = node
            self.__insert(node)
            self.size += 1


            # Your LRUCache object will be instantiated and called as such:
            # obj = LRUCache(capacity)
            # param_1 = obj.get(key)
            # obj.put(key,value)