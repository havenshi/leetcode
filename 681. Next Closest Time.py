# Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.
#
# You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.
#
# Example 1:
#
# Input: "19:34"
# Output: "19:39"
# Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours and 59 minutes later.
# Example 2:
#
# Input: "23:59"
# Output: "22:22"
# Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.

# class Solution(object):
#     def permute(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         array = [int(x) for x in nums if x != ':']
#
#         self.result = []
#         array.sort()
#         for i in range(len(array)):
#             length = len(array)
#             self.recursive_comb([array[i]], array[:i] + array[i + 1:], length)
#
#         index = self.result.index(nums)
#         if index + 1 >= len(self.result):
#             return self.result[index]
#         return self.result[index + 1]
#
#     def recursive_comb(self, temp_array, rest_array, target):
#         if len(temp_array) == target:
#             res = str(temp_array[0]) + str(temp_array[1]) + ':' + str(temp_array[2]) + str(temp_array[3])
#             if int(res[:2]) <= 24 and int(res[3:]) <= 60 and res not in self.result:
#                 self.result.append(res)
#         else:
#             for i in range(len(rest_array)):
#                 temp_array2 = temp_array[:]
#                 temp_array2.append(rest_array[i])
#                 self.recursive_comb(temp_array2, rest_array[:i] + rest_array[i + 1:], target)


    # method 2
class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        time = time[:2] + time[3:]
        isValid = lambda t: int(t[:2]) < 24 and int(t[2:]) < 60
        stime = sorted(time)
        for x in [3, 2, 1, 0]:
            for y in stime:
                if y <= time[x]: continue
                ntime = time[:x] + y + (stime[0] * (3 - x)) #该位替换一个较大值，然后把后面所有数位全部改成最小值
                if isValid(ntime): return ntime[:2] + ':' + ntime[2:]
        return stime[0] * 2 + ':' + stime[0] * 2

if __name__ == "__main__":
    answer = Solution()
    print answer.nextClosestTime('23:59')
    print answer.nextClosestTime('00:01')
    print answer.nextClosestTime('12:34')

