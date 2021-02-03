class Solution:
    def isHappy(self, n: int) -> bool:
        n = str(n)
        for i in range(1000):
            
            n = list(n)
            
            for j in range(len(n)):
                n[j] = int(n[j])**2
            
            final = sum(n)
            
            if final == 1:
                return True
            
            n = str(final)
        return False
