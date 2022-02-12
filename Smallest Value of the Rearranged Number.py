class Solution(object):
    def smallestNumber(self, num):
        if num > 0:
            digit_list = list(map(int, str(num)))
            digit_list.sort()
            if digit_list[0] == 0:
                for i in range(len(digit_list)):
                    if digit_list[i] != 0:
                        digit_list[0] = digit_list[i]
                        digit_list[i] = 0
                        break
            res = int("".join(map(str, digit_list)))
            return res
        else:
            num = abs(num)
            digit_list = list(map(int, str(num)))
            digit_list.sort(reverse = True)
            res = int("".join(map(str, digit_list)))
            return -1*res
        """
        :type num: int
        :rtype: int
        """
        
