class Solution(object):
    
    def arrangeCoins(self, n):
        ans = int((2*n + 0.25)**(0.5) - 0.5)
        return ans
