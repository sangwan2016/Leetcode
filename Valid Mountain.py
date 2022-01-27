class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        number = max(arr)
        if arr.index(number) == len(arr)-1:
            return True
            quit()
        if arr.index(number) == 0:
            return False
            quit()
        for i in range(arr.index(number)):
            if arr[i] < arr[i+1]:
                pass
            else:
                return False
                quit()
        for i in range(len(arr)-arr.index(number)):
            if arr[i] > arr[i+1]:
                pass
            else:
                return False
                quit()
        return True