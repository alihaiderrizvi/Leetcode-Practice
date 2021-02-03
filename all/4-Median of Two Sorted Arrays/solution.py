class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_list = (nums1 + nums2)
        new_list.sort()
        if len(new_list) %2 == 0:
            return (new_list[len(new_list)//2 - 1] + new_list[len(new_list)//2])/2
        return new_list[len(new_list)//2]
