class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = [i]
            else:
                d[nums[i]].append(i)
        
        for v in d.values():
            if len(v) > 1:
                v.sort()
                
                for i in range(len(v)-1):
                    
                    if abs(v[i+1] - v[i]) <= k:
                        return True
        return False
