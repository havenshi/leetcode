import re


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        prec = {}
        prec["*"] = 3
        prec["/"] = 3
        prec["+"] = 2
        prec["-"] = 2
        prec["("] = 1
        opStack = []
        postfixList = []
        tmp = s.strip().replace(" ", "")
        tokenList = re.split("([-()+*/])", tmp)
        tokenList = [x for x in tokenList if x]
        if len(tokenList) == 1: return int(tokenList[0])

        for token in tokenList:
            if token.isdigit():
                postfixList.append(token)
            elif token == '(':
                opStack.append(token)
            elif token == ')':
                topToken = opStack.pop()
                while topToken != '(':
                    postfixList.append(topToken)
                    topToken = opStack.pop()
            else:
                while opStack and (prec[opStack[-1]] >= prec[token]):
                    postfixList.append(opStack.pop())
                opStack.append(token)

        while opStack:
            postfixList.append(opStack.pop())
        return self.postfixEval(" ".join(postfixList))

    def postfixEval(self, postfixExpr):
        operandStack = []
        tokenList = postfixExpr.split()

        for token in tokenList:
            if token.isdigit():
                operandStack.append(int(token))
            else:
                operand2 = operandStack.pop()
                operand1 = operandStack.pop()
                result = self.doMath(token, operand1, operand2)
                operandStack.append(result)
        return operandStack.pop()

    def doMath(self, op, op1, op2):
        if op == "*":
            return op1 * op2
        elif op == "/":
            return op1 / op2
        elif op == "+":
            return op1 + op2
        else:
            return op1 - op2

if __name__ == '__main__':
    print Solution().calculate('2-1 + 22')