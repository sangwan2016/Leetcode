class Solution(object):
    def intToRoman(self, num):
        save_num = str(num) 
        num1 = numa = numb = numc = numd = nume = numf = num2 = num3 = num4 = num5 = num6 = num7 = 0 
        while True:
            if num >= 1000:
                num1 = num // 1000
                num -= num1*1000
            elif 1000 > num >= 500:
                if 900 <= num:
                    numa = num // 900
                    num -= numa*900
                else:
                    num2 = num // 500
                    num -= num2*500
            elif 100 <= num < 500:
                if 400 <= num:
                    numb = num // 400
                    num -= numb*400
                else:
                    num3 = num // 100
                    num -= num3*100
            elif 50 <= num < 100:
                if 90 <= num:
                    numc = num // 90
                    num -= numc*90
                else:
                    num4 = num // 50
                    num -= num4*50
            elif 10 <= num < 50:
                if 40 <= num:
                    numd = num // 40
                    num -= numd*40
                else:
                    num5 = num // 10
                    num -= num5*10
            elif 5 <= num < 10:
                if 9 <= num :
                    nume = num //9
                    num -= nume*9
                else:
                    num6 = num // 5
                    num -= num6*5
            elif 1 <= num < 5:
                if 4 <= num:
                    numf = num // 4
                    num -= numf*4
                else:
                    num7 = num // 1
                    num -= num7*5
            else:
                break
        answer = num1 * 'M' + numa * 'CM' + num2 * 'D' + numb * 'CD' + num3 * 'C' + numc * 'XC' + num4 * 'L' + numd * 'XL' + num5 * 'X' + nume * 'IX' + num6 * 'V' + numf * 'IV' + num7 * 'I'
        return answer
        """
        class Solution(object):
    def intToRoman(self, num):
        res = ""
        table = [
          (1000, "M"),
          (900, "CM"),
          (500, "D"),
          (400, "CD"),
          (100, "C"),
          (90, "XC"),
          (50, "L"),
          (40, "XL"),
          (10, "X"),
          (9, "IX"),
          (5, "V"),
          (4, "IV"),
          (1, "I"),
       ]
        for cap, roman in table:
            d, m = divmod(num, cap)
            res += roman * d
            num = m
        return res
        """
            
                
                
                
        :type num: int
        :rtype: str
        """
            
                
                
                
        :type num: int
        :rtype: str
        """
        
