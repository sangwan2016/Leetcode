class Solution(object):
    def removeElement(self, nums, val):
        remove_nums = nums.count(val)
        for i in range(remove_nums):
            nums.remove(val)
            
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
