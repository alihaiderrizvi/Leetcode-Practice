class Solution:
    def titleToNumber(self, s: str) -> int:
        a = 0
        power = 0
        for x in s[::-1]:
            a += (ord(x)-64)*(26**power)
            power+= 1
        return a
