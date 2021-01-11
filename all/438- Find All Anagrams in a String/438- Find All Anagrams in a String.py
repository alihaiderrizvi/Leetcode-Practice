import collections
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        p_counter = collections.Counter(p)
        l = len(p)
        ans = []
        
        for i in range(len(s)-l+1):
            s_counter = collections.Counter(s[i:i+l])
            if s_counter == p_counter:
                ans.append(i)
        
        return ans
