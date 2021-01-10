import collections

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_c = collections.Counter(s)
        t_c = collections.Counter(t)
        
        ans = t_c - s_c
        return list(ans.keys())[0]
