class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        dup = [i for i in range(1, len(nums)+1)]
        total_dup = sum(dup)
        
        diff = total_dup - total
        
        nums.sort()
        
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                elem = nums[i]
                break
        
        return [elem, elem + diff]
