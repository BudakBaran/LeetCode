        var nums1Index = m-1;
        var nums2Index = n-1;
        var index = m+n-1;

        while (nums2Index >= 0)
        {
            if (nums1Index >= 0 && nums1[nums1Index] > nums2[nums2Index])
            {
                nums1[index--] = nums1[nums1Index--];
            }
            else
            {
                nums1[index--] = nums2[nums2Index--];
            }
        }