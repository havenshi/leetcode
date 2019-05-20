import random
import string


class Codec:
    def __init__(self):
        self.full_tiny = {}  # 长URL：短URL
        self.tiny_full = {}  # 短URL：长URL

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        if longUrl in self.full_tiny:
            return "http://tinyurl.com/" + self.full_tiny[longUrl]
        else:
            suffix = self.six_addr()
            self.full_tiny[longUrl] = suffix
            self.tiny_full[suffix] = longUrl
            return "http://tinyurl.com/" + suffix

    def six_addr(self):  # 随机生成6个字符
        letters = string.ascii_letters + string.digits  # 62个字母加数字
        ans = ''
        tmp = ''
        for i in range(6):
            tmp = letters[random.randint(0, 10000) % 62]
            ans = ans + tmp
        return ans

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        shortUrl = shortUrl.split('/')[-1]
        if shortUrl in self.tiny_full:
            return self.tiny_full[shortUrl]
        else:
            return None

            # Your Codec object will be instantiated and called as such:
            # codec = Codec()
            # codec.decode(codec.encode(url))