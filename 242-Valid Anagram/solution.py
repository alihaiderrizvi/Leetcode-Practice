class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t = list(t)
        s = list(s)
        t = sorted(t)
        s = sorted(s)
        if s == t:
            return True
        return False
