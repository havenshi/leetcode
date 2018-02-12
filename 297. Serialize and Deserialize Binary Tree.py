# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        self.res = []
        self.helper(root)
        return ' '.join(self.res)

    def helper(self, node):
        if node:
            self.res.append(str(node.val))
            self.helper(node.left)  # first restore left tree, and then right tree
            self.helper(node.right)
        else:
            self.res.append('#')

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        self.data = data.split()  # convert '1 2 3' to iter, then can use next function
        return self.helper2()

    def helper2(self):
        val = self.data.pop(0)
        if val == '#':
            return None
        node = TreeNode(int(val))
        node.left = self.helper2()
        node.right = self.helper2()
        return node


    # def serialize(self, root):
    #     """Encodes a tree to a single string.
    #
    #     :type root: TreeNode
    #     :rtype: str
    #     """
    #
    #     def doit(node):
    #         if node:
    #             vals.append(str(node.val))
    #             doit(node.left)  # first restore left tree, and then right tree
    #             doit(node.right)
    #         else:
    #             vals.append('#')
    #
    #     vals = []
    #     doit(root)
    #     return ' '.join(vals)
    #
    # def deserialize(self, data):
    #     """Decodes your encoded data to tree.
    #
    #     :type data: str
    #     :rtype: TreeNode
    #     """
    #
    #     def doit():
    #         val = next(vals)
    #         if val == '#':
    #             return None
    #         node = TreeNode(int(val))
    #         node.left = doit()
    #         node.right = doit()
    #         return node
    #
    #     vals = iter(data.split())  # convert '1 2 3' to iter, then can use next function
    #     return doit()

        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.deserialize(codec.serialize(root))