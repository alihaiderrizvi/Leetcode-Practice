class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        while True:
            try:
                if nums[0] == nums[1] and nums[0] == nums[2]:
                    nums.pop(0)
                    nums.pop(0)
                    nums.pop(0)
                else:
                    return nums[0]
            except:
                return nums[0]
