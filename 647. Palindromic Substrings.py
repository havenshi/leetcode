class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        n  = len(s)
        for i in range(0, n):
            # itself
            res += 1
            # odds
            left = i -1
            right = i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
                res += 1
            # evens
            left = i
            right = i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
                res += 1
        return res

        # TLE
        # length = len(s)
        # res = 0
        #
        # # odd sublength
        # dictionary = {i: s[i] for i in range(length)}
        # res += sum([1 for v in dictionary.values() if v])
        # for sublength in range(3, length+1, 2):
        #     mid = sublength / 2
        #     for k, v in dictionary.items():
        #         if k in range(mid, length - mid) and v and s[k - mid] == s[k + mid]:
        #             dictionary[k] = s[k - mid] + v + s[k + mid]
        #             res += 1
        #         else:
        #             del dictionary[k]
        #
        # # even sublength
        # dictionary = {i: s[i:i+2] if s[i]==s[i+1] else None for i in range(length-1)}
        # res += sum([1 for v in dictionary.values() if v])
        # for sublength in range(4, length + 1, 2):
        #     mid = sublength / 2 - 1
        #     for k, v in dictionary.items():
        #         if k in range(mid, length - mid - 1) and v and s[k - mid] == s[k + mid + 1]:
        #             dictionary[k] = s[k - mid] + v + s[k + mid + 1]
        #             res += 1
        #         else:
        #             del dictionary[k]
        #
        # return res

if __name__ == '__main__':
    print Solution().countSubstrings('aaa')