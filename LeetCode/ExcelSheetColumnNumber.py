class Solution:
    def titleToNumber(self, s: str) -> int:
        res = i = 0
        while i < len(s):
            res += (26 ** (len(s) - 1 - i)) * (ord(s[i]) - ord('A') + 1)  # res = 679 + 26 ^ 2 * 26
            i += 1
        return res