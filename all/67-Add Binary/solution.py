class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num1 = 0
        num2 = 0
        a = a[::-1]
        b = b[::-1]
        
        #for A
        for i in range(len(a)):
            num1 += int(a[i]) * (2**i)
        
        #for B
        for i in range(len(b)):
            num2 += int(b[i]) * (2**i)
        
        C = num1 + num2
        
        ans = ""
        
        while C > 1:
            ans += str(C % 2)
            C = C // 2
            
        ans += str(C)
        return ans[::-1]
