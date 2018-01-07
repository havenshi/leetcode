# -*- coding: utf-8 -*-

# class Solution(object):
#     def sorter(self, x, y):
#         if x[0] != y[0]:
#             return x[0] - y[0]
#         return x[1] - y[1]
#
#
#     def heap_sort(self, ary): # fist item is the maximum
#         n = len(ary)
#         first = int(n / 2 - 1)
#         for start in range(first, -1, -1):
#             self.max_heapify(ary, start, n - 1)
#         return ary
#
#     def max_heapify(self, ary, start, end):
#         root = start
#         while True:
#             child = root * 2 + 1
#             if child > end: break
#             if child + 1 <= end and ary[child][2] < ary[child + 1][2]:
#                 child = child + 1
#             if ary[root][2] < ary[child][2]:
#                 ary[root], ary[child] = ary[child], ary[root]
#                 root = child
#             else:
#                 break
#
#
#     def getSkyline(self, buildings):
#         """
#         :type buildings: List[List[int]]
#         :rtype: List[List[int]]
#         """
#         # delete duplicate
#         newb = []
#         for building in buildings:
#             if building not in newb:
#                 newb.append(building)
#         buildings = newb
#
#         array = []
#         for building in buildings:
#             array.append((building[0], 1, building[2], building))
#             array.append((building[1], -1, building[2], building))
#         array = sorted(array, cmp=self.sorter)
#         # array = [(2, 1, 10, [2, 9, 10]), (3, 1, 15, [3, 7, 15]), (5, 1, 12, [5, 12, 12]), (7, -1, 15, [3, 7, 15]), (9, -1, 10, [2, 9, 10]),
#         # (12, -1, 12, [5, 12, 12]), (15, 1, 10, [15, 20, 10]), (19, 1, 8, [19, 24, 8]), (20, -1, 10, [15, 20, 10]), (24, -1, 8, [19, 24, 8])]
#         # print array
#
#         answer = []
#         heap = []
#         for i in range(len(array)):
#             if array[i][1] == 1: # if left line, push building to heap
#                 # attention, if add(2,3), must delete(2,0) first
#                 if answer and array[i][0] == answer[-1][0] and answer[-1][1] == 0:
#                     del answer[-1]
#                 # attention, if add(1,2), must delete(1,1) first
#                 if answer and array[i][0] == answer[-1][0] and array[i][2] >= answer[-1][1]:
#                     del answer[-1]
#                 # attention, if add(2,3), and last item of answer is (0,3), not add
#                 if (heap == [] or array[i][2] > heap[0][2]) and (answer == [] or array[i][2] != answer[-1][1]): # if the ith height > max of heap, add point to answer
#                     answer.append([array[i][3][0], array[i][3][2]])
#                 heap.append(array[i][3])
#                 heap = self.heap_sort(heap)
#             else: # if right line, delete the left line with the same height from heap
#                 index = heap.index(array[i][3])
#                 del heap[index]
#                 heap = self.heap_sort(heap)
#                 if len(heap) == 0: # if only one item in heap, add point to answer
#                     while answer and answer[-1][0] == array[i][0] and answer[-1][1] >= 0:
#                         del answer[-1]
#                     answer.append([array[i][3][1], 0])
#                 else:
#                     if array[i][3][2] > heap[0][2]:# if height greater than maximum height from heap, add point
#                         answer.append([array[i][3][1], heap[0][2]])
#             #print heap,answer
#
#         return answer


class MaxHeap: # 构造max堆，使最上层为最大值而非最小值，时间复杂度O(lgn)
    def __init__(self, buildings):
        self.buildings = buildings
        self.size = 0
        self.heap = [None] * (2 * len(buildings) + 1)
        self.lineMap = dict()
    def maxLine(self):
        return self.heap[1]
    def insert(self, lineId):
        self.size += 1
        self.heap[self.size] = lineId
        self.lineMap[lineId] = self.size
        self.siftUp(self.size)
    def delete(self, lineId):
        heapIdx = self.lineMap[lineId]
        self.heap[heapIdx] = self.heap[self.size]
        self.lineMap[self.heap[self.size]] = heapIdx
        self.heap[self.size] = None
        del self.lineMap[lineId]
        self.size -= 1
        self.siftDown(heapIdx)
    def siftUp(self, idx):
        while idx > 1 and self.cmp(idx / 2, idx) < 0:
            self.swap(idx / 2, idx)
            idx /= 2
    def siftDown(self, idx):
        while idx * 2 <= self.size:
            nidx = idx * 2
            if idx * 2 + 1 <= self.size and self.cmp(idx * 2 + 1, idx * 2) > 0:
                nidx = idx * 2 + 1
            if self.cmp(nidx, idx) > 0:
                self.swap(nidx, idx)
                idx = nidx
            else:
                break
    def swap(self, a, b):
        la, lb = self.heap[a], self.heap[b]
        self.lineMap[la], self.lineMap[lb] = self.lineMap[lb], self.lineMap[la]
        self.heap[a], self.heap[b] = lb, la
    def cmp(self, a, b):
        return self.buildings[self.heap[a]][2] - self.buildings[self.heap[b]][2]

class Solution:
    def getSkyline(self, buildings):
        size = len(buildings)
        points = sorted([(buildings[x][0], x, 's') for x in range(size)] +
                        [(buildings[x][1], x, 'e') for x in range(size)])
        maxHeap = MaxHeap(buildings)
        ans = []
        for p in points:
            # 首先把start line 或 end line 加到heap里
            if p[2] == 's':
                maxHeap.insert(p[1])
            else:
                maxHeap.delete(p[1])
            maxLine = maxHeap.maxLine() # 找到堆最顶端的值
            height = buildings[maxLine][2] if maxLine is not None else 0
            if len(ans) == 0 or ans[-1][0] != p[0]: # 如果是第一个line或者start value不与answer最后一个元素的start value重合，answer里加该line
                ans.append([p[0], height]) # 如果新元素height较高，则加的位正确新元素；否则新元素实际上在别的更高的building里面，加进去时使用了更高的height，该无效元素在下面的ans.pop()中删除
            # 如果与answer最后一个元素的start value重合
            elif p[2] == 's': # 新加start line的height为上升阶梯，则要不断拉高answer中最后一个元素的height
                ans[-1][1] = max(ans[-1][1], height)
            else: # 新加end line的height为下降阶梯，则要不断压低answer中最后一个元素的height
                ans[-1][1] = min(ans[-1][1], height)
            if len(ans) > 1 and ans[-1][1] == ans[-2][1]: # 如果此时answer里面最后两个元素有相同的height，如(0,3)(2,3)，删后一个
                ans.pop()
        return ans


if __name__=='__main__':
    answer = Solution()
    print answer.getSkyline([ [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ] )
    print answer.getSkyline([[0,2,3],[2,5,3]])
    print answer.getSkyline([[1, 2, 1], [1, 2, 2], [1, 2, 3]])
    print answer.getSkyline([[1, 5, 3], [1, 5, 3], [1, 5, 3]])
    print answer.getSkyline([[4, 10, 10], [5, 10, 9], [6, 10, 8], [7, 10, 7], [8, 10, 6], [9, 10, 5]])