class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        if len(nums) == 0:
            return False
        curr = nums[0]
        for i in nums[1:]:
            if i == curr:
                return True
            else:
                curr = i
        return False
