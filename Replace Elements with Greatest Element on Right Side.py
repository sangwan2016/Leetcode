class Solution(object):
    def replaceElements(self, arr):
        if 1 > len(arr) or len(arr) > 10**4:
            print("잘못된 list")
        for i in range(len(arr)):
            if 1 > arr[i] or arr[i] > 10**5:
                print("잘못된 list")
        if len(arr) == 1:
            arr[0] = -1
        else:
            for i in range(len(arr)):
                if i == len(arr)-1:
                    arr[i] = -1
                else:
                    arr[i] = max(arr[i+1:])
                
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        
