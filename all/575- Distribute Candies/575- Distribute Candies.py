class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        s = set()
        
        for i in candyType:
            s.add(i)
            
        return min(len(s), len(candyType)//2)
