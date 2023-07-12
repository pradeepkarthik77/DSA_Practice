class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        copyarr = nums1[:m].copy()

        i = 0
        j = 0
        indx = 0

        while i<m and j<n:

            if copyarr[i] < nums2[j]:
                nums1[indx] = copyarr[i]
                indx+=1
                i+=1
            else:
                nums1[indx] = nums2[j]
                j+=1
                indx+=1
        
        if i == m:
            while j<n:
                nums1[indx] = nums2[j]
                j+=1
                indx+=1
        
        if j == n:
            while i<m:
                nums1[indx] = copyarr[i]
                i+=1
                indx+=1
