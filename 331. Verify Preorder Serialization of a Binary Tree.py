class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        preorder = preorder.split(',')
        preorder = [p if p == '#' else int(p) for p in preorder]
        n = len(preorder)

        if preorder == ['#']:
            return True
        if n <= 2:
            return False

        stack = []
        for i in range(n):
            p = preorder[i]
            if type(p) == int:
                stack.append(p)
            else:
                if not stack or stack == ['#']:
                    return False
                else:
                    if type(stack[-1]) == int:
                        stack.append(p)
                    else:
                        # pop 1 and '#', and append this '#'. continue to pop all of its parents
                        stack.append(p)
                        while len(stack) >= 3 and stack[-2:] == ['#', '#']:
                            stack.pop()
                            stack.pop()
                            stack.pop()
                            stack.append(p)

        if stack == ['#']:
            return True
        else:
            return False

if __name__ == "__main__":
    answer=Solution()
    print answer.isValidSerialization("9,3,4,#,#,1,2,#,7,#,#,#,2,#,6,#,#")
    print answer.isValidSerialization("9,3,4,#,#,1,2,#,7,#,#,2,#,6,#,#")
    print answer.isValidSerialization("1,#,#,#,#")
    print answer.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#")