indexSec = 0
        for index in range(m+n):
            if(indexSec == n):
                break
            if nums1[index] == nums2[indexSec]:
                nums1.insert(index, nums2[indexSec])
                nums1.pop(len(nums1)-1)
                index = index - 1
                indexSec = indexSec + 1
            elif nums1[index] > nums2[indexSec]:
                nums1.insert(index, nums2[indexSec])
                index = index - 1
                indexSec = indexSec + 1
                nums1.pop(len(nums1)-1)
        for index in range(indexSec,n):
            nums1[m+index] = nums2[index]