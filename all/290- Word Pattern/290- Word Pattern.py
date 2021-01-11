class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d1 = defaultdict(set)
        d2 = defaultdict(set)
        s = s.split()
        
        if len(s) != len(pattern):
            return False
        
        for i in range(len(pattern)):
            d1[pattern[i]].add(s[i])
            d2[s[i]].add(pattern[i])
        
        l1 = list(d1.values())
        l2 = list(d2.values())
        
        for i in l1:
            if len(i) > 1:
                return False
        for i in l2:
            if len(i) > 1:
                return False
        return True
