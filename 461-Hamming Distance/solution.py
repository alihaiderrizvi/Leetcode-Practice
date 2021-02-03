class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a = ''
        b = ''
        
        a = bin(x)[2:]
        b = bin(y)[2:]
        
        if len(a) < len(b):
            a = "0"*(len(b)-len(a)) + a 
        if len(b) < len(a):
            b = "0"*(len(a)-len(b)) + b
        out = 0
        
        for c,d in zip(a,b):
            if c != d:
                out+=1
        return out
