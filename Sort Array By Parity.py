class Solution(object):
    def sortArrayByParity(self, nums):
        nums1 = nums[:]
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                nums1.remove(nums[i])
                nums1.append(nums[i])
        return nums1
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
