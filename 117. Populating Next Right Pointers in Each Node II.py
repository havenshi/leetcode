# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root:
            if root.left and root.right:
                root.left.next = root.right
                tmp = root.next
                while tmp:
                    if tmp.left:
                        root.right.next = tmp.left
                        break
                    if tmp.right:
                        root.right.next = tmp.right
                        break
                    tmp = tmp.next
            elif root.left:
                tmp = root.next
                while tmp:
                    if tmp.left:
                        root.left.next = tmp.left
                        break
                    if tmp.right:
                        root.left.next = tmp.right
                        break
                    tmp = tmp.next
            elif root.right:
                tmp = root.next
                while tmp:
                    if tmp.left:
                        root.right.next = tmp.left
                        break
                    if tmp.right:
                        root.right.next = tmp.right
                        break
                    tmp = tmp.next
            self.connect(root.right) # right recursion should be the first
            self.connect(root.left)

            #  4->5->6
            # /       \
            #7         8
            # 为什么先要遍历root.right呢？例如4->5->6，如果right的5没有跟next的6接上，在递归left的4时，寻找root.next就会在5停止。而实际上4的child7是可以跟next.next6的child8接上的，出现错误。