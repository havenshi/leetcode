class Solution(object):
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        days = [0] * len(flowers)
        for i in range(len(flowers)):
            days[flowers[i] - 1] = i  # days = [1, 4, 0, 3, 2], which flower bloom on that day

        dict = {}
        length = 0
        array = []


        i, left, right = 0, 0, k + 1
        while right < len(days):
            for l in dict:
                if days[i] > l and days[i] < dict[l]:
                    del dict[l]
                    length -= 1

            if days[i] > days[left] and days[i] > days[right]:
                pass # not influence pair
            elif days[i] < max(days[left], days[right]) and days[i] > min(days[left], days[right]):
                left = right
                right = k + 1 + left

            if days[i] == days[right]:
                dict[min(days[left],days[right])] = max(days[left],days[right])
                length += 1
                left = right
                right = k + 1 + left

            array.append(length)
            i += 1
            print array,dict
        return array

if __name__ == "__main__":
    answer = Solution()
    print answer.kEmptySlots([3,1,5,4,2], 1)
