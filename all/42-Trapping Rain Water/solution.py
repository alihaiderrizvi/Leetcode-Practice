class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        
        l1 = []
        l2 = []
        final = []
        vol = 0
        
        elem = height[0]
        
        for i in height:
            if i > elem:
                elem = i
            l1.append(elem)
        
        height = height[::-1]
        elem = height[0]
        
        for i in height:
            if i > elem:
                elem = i
            l2.append(elem)
        
        l2 = l2[::-1]
        height = height[::-1]
        
        for i,j in zip(l1,l2):
            final.append(min(i, j))
        
        for i, j in zip(final, height):
            vol += abs(i - j)
        
        return vol
