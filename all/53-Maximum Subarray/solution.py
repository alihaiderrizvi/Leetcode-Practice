class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_yet = cur_best = nums[0]
        for i in range(1, len(nums)):
            cur_best = max(nums[i], cur_best+ nums[i])
            if cur_best > best_yet:
                best_yet = cur_best
        return best_yet
