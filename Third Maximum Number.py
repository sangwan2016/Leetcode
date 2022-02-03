class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            nums.sort()
            return nums[1]
        else:
            length = len(nums)
            nums.sort(reverse=True)
            num1 = nums.count(nums[0])
            if num1 == length:
                return nums[0]
            num2 = nums.count(nums[num1])
            if num1 + num2 == length:
                return nums[0]
            else:
                for i in range(num1+num2):
                    nums.remove(nums[0])
                return nums[0]
            
