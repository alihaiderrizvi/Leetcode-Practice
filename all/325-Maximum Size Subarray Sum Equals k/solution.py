class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        d = {0:-1}
        
        rs = 0
        ans = 0
        
        for ind,num in enumerate(nums):
            rs += num
            
            if rs-k in d:
                ans = max(ans, ind - d[rs-k])
            
            if rs not in d:
                d[rs] = ind
        
        return ans
