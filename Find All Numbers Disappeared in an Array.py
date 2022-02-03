class Solution(object):
    def findDisappearedNumbers(self, nums):
        size = len(nums)
        num1 = range(1,size+1)
        return list(set(num1) - set(nums))
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
