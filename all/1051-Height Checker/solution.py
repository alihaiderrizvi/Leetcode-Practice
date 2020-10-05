class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        heights_copy = sorted(heights)
        
        for i,j in zip(heights, heights_copy):
            if i != j:
                count += 1
        
        return count
