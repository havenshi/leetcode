# You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend
#
#  take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person
#
# will be the winner.
#
# Write a function to determine if the starting player can guarantee a win.
#
# For example, given s = "++++", return true. The starting player can guarantee a win by flipping the middle "++" to become "+--+".
#
# Follow up:
# Derive your algorithm's runtime complexity.
class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, n = 0, len(s) - 1
        is_win = False
        while not is_win and i < n:  # O(n) time
            if s[i] == '+':
                while not is_win and i < n and s[i + 1] == '+':  # O(c) time
                    # t(n, c) = c * (t(n, c-1) + n) + n = ...
                    # = c! * t(n, 0) + n * c! * (c + 1) * (1/0! + 1/1! + ... 1/c!)
                    # = n * c! + n * c! * (c + 1) * O(e) = O(c * n * c!)
                    is_win = not self.canWin(s[:i] + '--' + s[i + 2:])  # O(n) space
                    i += 1
            i += 1
        return is_win