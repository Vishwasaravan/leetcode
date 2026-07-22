class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        x=nums1[0:m]
        y=nums2[0:n]
        nums1[:]=sorted(x+y)
        