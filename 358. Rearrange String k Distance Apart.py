# Given a non-empty string str and an integer k, rearrange the string such that the same characters are at least distance k from each other.
#
# All input strings are given in lowercase letters. If it is not possible to rearrange the string, return an empty string "".
#
# Example 1:
# str = "aabbcc", k = 3
#
# Result: "abcabc"
#
# The same letters are at least distance 3 from each other.
# Example 2:
# str = "aaabc", k = 3
#
# Answer: ""
#
# It is not possible to rearrange the string.
# Example 3:
# str = "aaadbbcc", k = 2
#
# Answer: "abacabcd"
#
# Another possible answer is: "abcabcda"
#
# The same letters are at least distance 2 from each other.

# 其基本思想是贪心策略，我们首先统计每个字符出现的个数，然后用一个优先队列来组织它们，以便于出现个数多的字符优先被排列。具体做法如下：
#
# 1）如果剩余字符的数量大于等于k，那么我们优先排列这k个不同的字符。如果在排列的过程中发现并没有k个不同的字符了，
# 那么说明后面无论如何排列，都会有字符间隔小于k，所以可以直接返回空串。
#
# 2）如果剩余的字符数量小于k个呢？可以采用和1）一样的方法排列剩余的不同字符。
#
# 我们采用优先队列进行排列，可以保证让数量大的字符最优先得到排列，并且使其间隔的距离最小，
# 这样可以最大限度地保证后面的字符有足够大的自由排列空间。
#
# 如果写出来了下面的代码片段，那么还有一个考点就是如何计算该算法的时间复杂度？虽然在while循环里面还有一个for循环，
# 但是仔细分析我们就可以发现，所有循环的执行次数加起来刚好是字符串s的长度，因为每执行一次循环result的长度就增加1。
# 所以算法的时间复杂度是O(n)，空间复杂度是O(m)，m是s中不同字符的个数。