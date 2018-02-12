# Given a sorted array of integers nums and integer values a, b and c. Apply a function of the form f(x) = ax2 + bx + c to each element x in the array.
#
# The returned array must be in sorted order.
#
# Expected time complexity: O(n)
#
# Example:
# nums = [-4, -2, 2, 4], a = 1, b = 3, c = 5,
#
# Result: [3, 9, 15, 33]
#
# nums = [-4, -2, 2, 4], a = -1, b = 3, c = 5
#
# Result: [-23, -5, 1, 7]
# Credits:
# Special thanks to @elmirap for adding this problem and creating all test cases.

# 当a>0，说明两端的值比中间的值大，那么此时我们从结果res后往前填数，用两个指针分别指向nums数组的开头和结尾，指向的两个数就是抛物线两端的数，将它们之中较大的数先存入res的末尾，然后指针向中间移，重复比较过程，直到把res都填满。
#
# 当a<0，说明两端的值比中间的小，那么我们从res的前面往后填，用两个指针分别指向nums数组的开头和结尾，指向的两个数就是抛物线两端的数，将它们之中较小的数先存入res的开头，然后指针向中间移，重复比较过程，直到把res都填满。
#
# 当a=0，函数是单调递增或递减的，那么从前往后填和从后往前填都可以，我们可以将这种情况和a>0合并。