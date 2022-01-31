class Solution(object):
    def heightChecker(self, heights):
        indice = 0
        expected = sorted(heights)
        for i in range(len(heights)):
            if expected[i] != heights[i]:
                indice += 1
        return indice
        """
        :type heights: List[int]
        :rtype: int
        """
        
