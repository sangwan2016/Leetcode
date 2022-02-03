class Solution(object):
    def search(self, nums, target):
        l = 0
        r = len(nums)-1
        while True:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
            if l > r:
                return -1
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #Another code
        """
 class Solution(object):
    def search(self, nums, target):
        l = 0
        r = len(nums)-1
        if target in nums:
            return nums.index(target)
        else:
            return -1
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
