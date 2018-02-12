# A group of friends went on holiday and sometimes lent each other money. For example, Alice paid for Bill's lunch for 10.ThenlaterChrisgaveAlice10.ThenlaterChrisgaveAlice5 for a taxi ride. We can model each transaction as a tuple (x, y, z) which means person x gave person y $z. Assuming Alice, Bill, and Chris are person 0, 1, and 2 respectively (0, 1, 2 are the person's ID), the transactions can be represented as [[0, 1, 10], [2, 0, 5]].
#
# Given a list of transactions between a group of people, return the minimum number of transactions required to settle the debt.
#
# Note:
# A transaction will be given as a tuple (x, y, z). Note that x ≠ y and z > 0.
# Person's IDs may not be linear, e.g. we could have the persons 0, 1, 2 or we could also have the persons 0, 2, 6.
#
# Example 1:
#
# Input:
# [[0,1,10], [2,0,5]]
#
# Output:
# 2
#
# Explanation:
# Person #0 gave person #1 $10.
# Person #2 gave person #0 $5.
#
# Two transactions are needed. One way to settle the debt is person #1 pays person #0 and #2 $5 each.
#
# Example 2:
#
# Input:
# [[0,1,10], [1,0,1], [1,2,5], [2,0,5]]
#
# Output:
# 1
#
# Explanation:
# Person #0 gave person #1 $10.
# Person #1 gave person #0 $1.
# Person #1 gave person #2 $5.
# Person #2 gave person #0 $5.
#
# Therefore, person #1 only need to give person #0 $4, and all debt is settled.
#
# 这道题给了一堆某人欠某人多少钱这样的账单，问我们经过优化后最少还剩几个。其实就相当于一堆人出去玩，
# 某些人可能帮另一些人垫付过花费，最后结算总花费的时候可能你欠着别人的钱，其他人可能也欠你的欠。
# 我们需要找出简单的方法把所有欠账都还清就行了。这道题的思路跟之前那道Evaluate Division有些像，
# 都需要对一组数据颠倒顺序处理。我们使用一个哈希表来建立每个人和其账户的映射，其中账户若为正数，说明其他人欠你钱；
# 如果账户为负数，说明你欠别人钱。我们对于每份账单，前面的人就在哈希表中减去钱数，后面的人在哈希表中加上钱数。
# 这样我们每个人就都有一个账户了，然后我们接下来要做的就是合并账户，看最少需要多少次汇款。我们先统计出账户值不为0的人数，
# 因为如果为0了，表明你既不欠别人钱，别人也不欠你钱，如果不为0，我们把钱数放入一个数组accnt中，然后调用递归函数。
# 在递归函数中，我们初始化结果res为整型最大值，然后我们跳过为0的账户，然后我们开始遍历之后的账户，
# 如果当前账户和之前账户的钱数正负不同的话，我们将前一个账户的钱数加到当前账户上，这很好理解，比如前一个账户钱数是-5，
# 表示张三欠了别人五块钱，当前账户钱数是5，表示某人欠了李四五块钱，那么张三给李四五块，这两人的账户就都清零了。
# 然后我们调用递归函数，此时从当前改变过的账户开始找，num表示当前的转账数，需要加1，
# 然后我们用这个递归函数返回的结果来更新res，后面别忘了复原当前账户的值。遍历结束后，我们看res的值如果还是整型的最大值，
# 说明没有改变过，我们返回num，否则返回res即可