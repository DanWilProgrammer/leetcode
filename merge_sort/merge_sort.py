class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        #m = number of elements in nums1
        #n = number of elements in nums2
        
        #while nums2 is not an empty list
        while n > 0:
            #if nums1 is not an empty list and nums1 
            if m > 0 and nums1[m - 1] >= nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n-1]
                n -= 1
        """
        Do not return anything, modify nums1 in-place instead.
        """ 
