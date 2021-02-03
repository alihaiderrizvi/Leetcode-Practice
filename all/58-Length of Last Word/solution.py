class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        try:
            s = s.split()
            return len(s[-1])
        except:
            return 0
