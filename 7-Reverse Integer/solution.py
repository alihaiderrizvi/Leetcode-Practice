class Solution:
    def reverse(self, x: int) -> int:
        
            
        if x >= 0:
            a = (int(str(x)[::-1]))
            if a > 2**31 - 1 or a < (-2) ** 31:
                return 0
            else:
                return a
        else:
            a = int(str(x)[-1:0:-1]) * -1
            if a > 2**31 - 1 or a < (-2) ** 31:
                return 0
            else:
                return a
