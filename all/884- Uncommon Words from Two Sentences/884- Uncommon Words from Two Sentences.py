class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        d = defaultdict(int)
        
        A = A.split()
        B = B.split()
        
        for i in A:
            d[i] += 1
            
        for j in B:
            d[j] += 1
        
        l = []

        for k,v in d.items():
            if v == 1:
                l.append(k)
        
        l.sort()
        return l
        
