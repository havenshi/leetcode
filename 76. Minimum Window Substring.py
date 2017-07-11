# -*- coding: utf-8 -*-
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        count1={}
        count2={}
        for char in t:
            if char not in count1: count1[char]=1
            else: count1[char] += 1
        for char in t:
            if char not in count2: count2[char]=1
            else: count2[char] += 1

        count=len(t)
        start=0; minSize=100000; minStart=0
        for end in range(len(s)):
            if s[end] in count2 and count2[s[end]]>0: # 尾指针不断往后扫，当扫到有一个窗口包含了所有T的字符
                count1[s[end]]-=1
                if count1[s[end]]>=0: # 如果为-1或更小了，说明S里面T元素太多，count1多减了，所以不算数，故count无须-1
                    count-=1

            if count==0: # 此时end可以为"CODEBANC"中任意的数，因为从C开始之前的S中已经能找到ABC了
                while True: # 然后再收缩头指针，直到不能再收缩为止
                    if s[start] in count2 and count2[s[start]]>0:
                        if count1[s[start]]<0: # 把刚才多减的无效的S里面T元素加回来，并舍弃该位，start后移
                            count1[s[start]]+=1
                        else: # 最早出现的S里面T元素已经复位为0了，因为要求substring，此时要跳出，重新寻找end
                            break
                    start+=1
                # 此时s[start:end + 1]为
                # 0 5 ADOBEC
                # 0 6 ADOBECO
                # 0 7 ADOBECOD
                # 0 8 ADOBECODE
                # 0 9 ADOBECODEB
                # 5 10 CODEBA
                # 5 11 CODEBAN
                # 9 12 BANC
                if minSize>end-start+1:
                    minSize=end-start+1; minStart=start
        if minSize==100000: return ''
        else:
            return s[minStart:minStart+minSize]


if __name__ == "__main__":
    answer=Solution()
    print answer.minWindow("ADOBECODEBANC", "ABC")