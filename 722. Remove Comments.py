class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        res = []
        buffer = ''
        flag = False

        for line in source:
            i = 0
            while i < len(line):
                char = line[i]
                if flag:
                    if char == '*' and line[i:i + 2] == '*/':
                        flag = False
                        i += 1
                elif char == '/':
                    if line[i:i + 2] == '//':
                        break
                    elif line[i:i + 2] == '/*':
                        flag = True
                        i += 1
                    else:
                        buffer += char
                else:
                    buffer += char
                i += 1

            if buffer and not flag:
                res.append(buffer)
                buffer = ''
        return res