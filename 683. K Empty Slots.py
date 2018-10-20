# -*- coding:utf8 -*-
# There is a garden with N slots. In each slot, there is a flower. The N flowers will bloom one by one in N days. In each day, there will be exactly one flower blooming and it will be in the status of blooming since then.
#
# Given an array flowers consists of number from 1 to N. Each number in the array represents the place where the flower will open in that day.
#
# For example, flowers = x means that the unique flower that blooms at day i will be at position x, where i and x will be in the range from 1 to N.
#
# Also given an integer k, you need to output in which day there exists two flowers in the status of blooming, and also the number of flowers between them is k and these flowers are not blooming.
#
# If there isn't such day, output -1.
#
# Example 1:
# Input:
# flowers: [1,3,2]
# k: 1
# Output: 2
# Explanation: In the second day, the first and the third flower have become blooming.
# Example 2:
# Input:
# flowers: [1,2,3]
# k: 1
# Output: -1.
# Note:
# The given array will be in the range [1, 20000]


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        n = len(flowers)
        if n == 0 or k >= n:
            return -1

        left_dict = {}
        right_dict = {}
        length = 0
        array = [length]
        root = TreeNode(flowers[0])
        node = root

        # 1.判断pair
        for i in range(1, n):
            cur_flower = flowers[i]
            left_flower = cur_flower - k - 1
            if self.find(node, left_flower):
                tmp = self.find(node, left_flower).right
                # 注意最小公有parent必须是其中一个数，否则跨了BST，失效
                if not tmp and not (self.lowestCommonAncestor(node,cur_flower,left_flower) != cur_flower and self.lowestCommonAncestor(node,cur_flower,left_flower) != left_flower):
                    self.insert(node, cur_flower)
                    left_dict[left_flower] = cur_flower
                    right_dict[cur_flower] = left_flower
                    length += 1
                else:
                    while tmp and tmp.left:
                        tmp = tmp.left
                    # tmp的右子树的最左子节点，也就是右子树里面最小的必须要大于cur_flower
                    if tmp and tmp.val > cur_flower and not (self.lowestCommonAncestor(node,cur_flower,left_flower) != cur_flower and self.lowestCommonAncestor(node,cur_flower,left_flower) != left_flower):
                        left_dict[left_flower] = cur_flower
                        right_dict[cur_flower] = left_flower
                        length += 1

            cur_flower = flowers[i]
            right_flower = cur_flower + k + 1
            if self.find(node, right_flower):
                tmp = self.find(node, right_flower).left
                if not tmp and not (self.lowestCommonAncestor(node,cur_flower,right_flower) != cur_flower and self.lowestCommonAncestor(node,cur_flower,right_flower) != right_flower):
                    self.insert(node, cur_flower)
                    left_dict[cur_flower] = right_flower
                    right_dict[right_flower] = cur_flower
                    length += 1
                else:
                    while tmp and tmp.right:
                        tmp = tmp.right
                    if tmp and tmp.val < cur_flower and not (self.lowestCommonAncestor(node,cur_flower,right_flower) != cur_flower and self.lowestCommonAncestor(node,cur_flower,right_flower) != right_flower):
                        left_dict[cur_flower] = right_flower
                        right_dict[right_flower] = cur_flower
                        length += 1


            # 2.加进去后判断是否使dict中的pair invalid
            self.insert(node, cur_flower)

            parent = self.find_parent(node, cur_flower, None)
            # 如果parent比较大，则以parent为右边的pair失效
            if parent and parent.val != right_flower and cur_flower < parent.val and parent.val in right_dict:
                del left_dict[right_dict[parent.val]]
                del right_dict[parent.val]
                length -= 1

            elif parent and parent.val != left_flower and cur_flower > parent.val and parent.val in left_dict:
                del right_dict[left_dict[parent.val]]
                del left_dict[parent.val]
                length -= 1

            array.append(length)

            # print left_dict,right_dict, array

        if any(array) == 0:
            return -1
        else:
            return max([i for i in range(n-1,-1,-1) if array[i] != 0])+1




    def find(self, node, data):
        if (data == node.val):
            return node
        elif (data < node.val):
            if node.left:
                return self.find(node.left, data)
            else:
                return False
        else:
            if node.right:
                return self.find(node.right, data)
            else:
                return False

    def find_parent(self, node, data, parent):
        if (data == node.val):
            return parent
        elif (data < node.val):
            if node.left:
                parent = node
                return self.find_parent(node.left, data, parent)
            else:
                return False
        else:
            if node.right:
                parent = node
                return self.find_parent(node.right, data, parent)
            else:
                return False

    def insert(self, node, data):
        if node.val == data:
            return False  # As BST cannot contain duplicate data

        elif data < node.val:
            if node.left:
                return self.insert(node.left, data)
            else:
                node.left = TreeNode(data)
                return True

        else:
            if node.right:
                return self.insert(node.right, data)
            else:
                node.right = TreeNode(data)
                return True

    def lowestCommonAncestor(self, root, p, q):
        if root == None:
            return None
        if p >= q:
            p, q = q, p  # make sure p is smaller
        if p <= root.val and q >= root.val:
            # if root value is in the middle of p and q, return root.
            return root.val
        if p < root.val and q < root.val:
            return self.lowestCommonAncestor(root.left, p, q)  # common root must be on left
        if p > root.val and q > root.val:
            return self.lowestCommonAncestor(root.right, p, q)  # common root must be on right


        # method2
class Solution(object):
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        days = [0] * len(flowers)
        for i in range(len(flowers)):
            days[flowers[i]-1] = i # days = [1, 4, 0, 3, 2], which flower bloom on that day

        result = float("inf")
        i, left, right = 0, 0, k+1
        while right < len(days):
            # 如果i天的开花位置小于left或left+k+1天中的某一天的开花位置，left和right天需要成对移动1
            # 如果i天的开花位置大于left和left+k+1两天的开花位置，说明这个第i天在当前left和right天区间内不用考虑，可以直接i+1进行新一轮判断
            if days[i] < days[left] or days[i] <= days[right]:
                # 如果i天已经到达了right天
                if i == right:
                    result = min(result, max(days[left], days[right])) # 取符合条件的最小天数，这个天数为left和left+k+1天的开花位置最大值
                    print i,left,right,result
                left, right = i, k+1+i
            i += 1

        return -1 if result == float("inf") else result+1

if __name__ == "__main__":
    answer=Solution()
    print answer.kEmptySlots([3,1,5,4,2],1)
    print answer.kEmptySlots([1,2,3], 1)
    print answer.kEmptySlots([1,3,2], 1)

# 需要返回满足条件的最后一天而不是第一天。
# 比如：([3,1,5,4,2],1)
# leetcode原题应该返回2，但是变形后应该返回4。


def solution(P, K):
    len_P = len(P)
    if len_P <= 1 or K >= len_P - 1:
        return -1
    space_array = [0] * len_P
    left_array = [-1] * len_P
    right_array = [len_P] * len_P
    for i in range(1, len_P):
        left_array[i] = i-1
    for i in range(0, len_P-1):
        right_array[i] = i + 1
    # left_array=[-1, 0, 1, 2, 3]
    # right_array=[1, 2, 3, 4, 5]
    for i in range(len_P):
        position = P[i-1] - 1 #第几盆花bloom
        if position > 0 and position < len_P - 1: #如果种花的位置不是首位
            space_array[position] = 1 + space_array[position-1] + space_array[position+1]
            if space_array[position-1] != 0:
                left_array[position] = left_array[position-1]
                space_array[left_array[position]+1] = space_array[position]
            if space_array[position+1] != 0:
                right_array[position] = right_array[position+1]
                space_array[right_array[position]-1] = space_array[position]
            # if space_array[position] == K and left_array[position] != -1 and right_array[position] != len_P:
            #     return i - 1
        elif position == 0:
            space_array[position] = 1 + space_array[position+1]
            right_array[position] = right_array[position+1]
            space_array[right_array[position]-1] = space_array[position]
        elif position == len_P - 1:
            space_array[position] = 1 + space_array[position-1]
            left_array[position] = left_array[position-1]
            space_array[left_array[position]+1] = space_array[position]
        print  space_array , left_array,right_array
    return -1

def kv_solution(P, K):
    kv = {}
    len_p = len(P)
    for i in range(len_p - 1, -1, -1):
        position = P[i]
        kv[position] = position
        # 把左右边的空白位置接上
        low = kv.get(position-1, position)
        high = kv.get(position+1, position)
        kv[low] = high
        kv[high] = low
        print position,kv
        # high,low记录该位置不放花的时候，该位置左右边空白的位置
        # 2{2：2}
        # 4{2：2, 4：4}
        # 5{2：2, 4：5, 5：4}
        # 1{1：2，2：1, 4：5, 5：4}
        # 3{1：5, 2：1, 3：3, 4：5, 5：1}
        if abs(high - low)+1 == K and max(high, low) != len_p and min(high, low) != 1:
            return i
    return -1


if __name__ == "__main__":
    # print solution([3,1,5,4,2],1)
    print kv_solution([3,1,5,4,2],1)
    # print solution([1,2,3], 1)
    # print kv_solution([1,2,3], 1)
    # print solution([1,3,2], 1)
    # print kv_solution([1,3,2], 1)
    # print solution([], 5)
    # print kv_solution([], 5)
    # print solution([1,3,2], 0)
    # print kv_solution([1,3,2], 0)
    # print solution([1,3,5,7,9,8,6,4,2], 1)
    # print kv_solution([1,3,5,7,9,8,6,4,2], 1)
    # print solution([1,8,7,5,11,3,4,6,2,10,9], 2)
    # print kv_solution([1,8,7,5,11,3,4,6,2,10,9], 2)
    # print solution([1,8,7,5,11,4,3,6,9,10,2], 2)
    # print kv_solution([1,8,7,5,11,4,3,6,9,10,2], 2)
    # print solution([1,8,7,5,11,4,10,6,9,3,2], 3)
    # print kv_solution([1,8,7,5,11,4,10,6,9,3,2], 3)