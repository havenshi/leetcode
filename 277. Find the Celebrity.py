# Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity.
# The definition of a celebrity is that all the other n - 1people know him/her but he/she does not know any of them.
#
# Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do
# is to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B. You need to find out the
# celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).
#
# You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int
# findCelebrity(n), your function should minimize the number of calls to knows.
#
# Note: There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is
# a celebrity in the party. If there is no celebrity, return -1.

# 建立个一维数组用来标记每个人的名人候选状态，开始均初始化为true，表示每个人都是名人候选人，然后我们一个人一个人的验证其
# 是否为名人，对于候选者i，我们遍历所有其他人j，如果i认识j，或者j不认识i，说明i不可能是名人，那么我们标记其为false，
# 然后验证下一个候选者，反之如果i不认识j，或者j认识i，说明j不可能是名人，标记之。对于每个候选者i，如果遍历了一圈而
# 其候选者状态仍为true，说明i就是名人，返回即可，如果遍历完所有人没有找到名人，返回-1

# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):
#
# Time:  O(n^2)
# Space: O(1)
class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        candidate = [True]*n
        for i in range(n):
            if candidate[i]:
                for j in range(i+1, n):
                    if knows(i, j) or not knows(j, i):
                        candidate[i] = False
                        break
                    elif not knows(i, j) or knows(j, i):
                        candidate[j] = False
            if candidate[i]:
                return i
        return -1