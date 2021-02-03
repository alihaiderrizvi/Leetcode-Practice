class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        count = 0
        
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                count += 1
            else:
                i += 1
        
        for j in range(count):
            nums.append(0)
