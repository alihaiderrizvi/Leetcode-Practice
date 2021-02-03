class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        largest = 0
        while i < j:
            h = min(height[i], height[j])
            l = j-i
            if h*l > largest:
                largest = h*l
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return largest
