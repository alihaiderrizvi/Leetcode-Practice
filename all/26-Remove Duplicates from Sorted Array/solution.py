class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) > 0:
            cur = nums[0]
            l = 1
            while l < len(nums):
                if nums[l] == cur:
                    nums.pop(l)
                    l-=1
                else:
                    cur = nums[l]
                l+=1
            return len(nums)
        else:
            return 0
