# -*- coding: utf-8 -*-
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        import collections
        dictionary = collections.Counter(tasks)
        if n == 0: return len(tasks)

        res = 0
        max_key = max(dictionary, key=dictionary.get)
        max_val = max(dictionary.values())
        array = [1] * max_val  # 使用频率最大的字母组成[1,1,1...]
        del dictionary[max_key]

        while dictionary:
            max_key = max(dictionary, key=dictionary.get)
            max_val = max(dictionary.values())
            #  dictionary,array = Counter({'B': 3}) [1, 1, 1]

            if not array:  # 如果array全部被删完了，重新构造，并跳过后面的步骤
                array = [1] * max_val
                del dictionary[max_key]
                continue

            min_len = min(len(array), max_val)  # 取array长度和最大频率字母的最短长度
            for i in range(min_len):  # array每段长度不断加1，表示新的字母加进去；dict中频率也减1
                array[i] += 1
                dictionary[max_key] -= 1
            if array[min_len - 1] == (n + 1):  # 如果array每段长度达到了间隔n的要求，删除，并更新res
                res += array[i] * min_len
                del array[:min_len]
            if dictionary[max_key] == 0:
                del dictionary[max_key]
            else:  # 如果dict中还有该字母，重新构造新的片段并加入array的后面
                array += [1] * dictionary[max_key]
                del dictionary[max_key]

        if array:
            for i in range(len(array) - 1):
                res += (n + 1)  # 反正不满足间隔n的条件，所以该片段的长度一定为n+1
            res += array[len(array) - 1]
        return res

if __name__ == "__main__":
    print Solution().leastInterval(["A","A","A","B","B","B"], 2)