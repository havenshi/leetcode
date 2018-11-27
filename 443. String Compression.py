class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        n = len(chars)
        if n <= 1:
            return n

        value = chars[0]
        count = 1
        index = 0
        i = 1
        while i < n:
            if chars[i] != value:
                # first set the count of the last value
                if count > 1:
                    index += 1  # move index to the count position
                    digit = self.digit(count) - 1
                    while digit >= 0:
                        tmp = count / 10 ** digit
                        chars[index] = str(tmp)
                        count -= tmp * 10 ** digit
                        digit -= 1
                        index += 1
                    index -= 1  # adjust

                value = chars[i]
                index += 1
                if index >= len(chars):
                    chars.append(value)
                else:
                    chars[index] = value  # change value in chars

                count = 1  # 1 means no repeat
                i += 1

            else:
                count += 1
                i += 1

        # don't forget to set count of the last value
        if count > 1:
            index += 1
            digit = self.digit(count) - 1
            while digit >= 0:
                tmp = count / 10 ** digit
                chars[index] = str(tmp)
                count -= tmp * 10 ** digit
                digit -= 1
                index += 1
            index -= 1  # adjust

        while len(chars) > index + 1: chars.pop()
        print min(n, index + 1)

    def digit(self, n):
        count = 0
        while n > 0:
            count += 1
            n /= 10
        return count


class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        last, count, res = chars[0], 1, 0
        for i in range(1, len(chars)):
            cur = chars[i]
            if cur == last:
                count += 1
            else:
                for ch in last + str(count > 1 and count or ''): # ch = "a", "2"
                    chars[res] = ch
                    res += 1
                last, count = cur, 1
        for ch in last + str(count > 1 and count or ''): #处理最后的一段
            chars[res] = ch
            res += 1
        while len(chars) > res:
            chars.pop()
        return res