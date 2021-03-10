class Solution:
    def intToRoman(self, num: int) -> str:
        r = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M', 2:'II', 3:'III', 4:'IV', 6:'VI', 7:'VII',8:'VIII', 9:'IX',
            40: 'XL', 90: 'XC', 400: 'CD', 900 : 'CM'}
        
        x = "" 
        while(num > 0):    
            if num >= 40 and num < 50: 
                x += r[40] 
                num -= 40 
            elif num >= 90 and num < 100: 
                x += r[90]
                num -= 90 
            elif num >= 400 and num < 500:
                x += r[400]
                num -= 400 
            elif num >= 900 and num < 1000: 
                x += r[900] 
                num -=900 
            elif num <= 10: 
                x += r[num]
                num -= num 
            elif num >= 10 and num < 40: 
                x += r[10]
                num -= 10 
            elif num >= 50 and num < 90: 
                x += r[50] 
                num -= 50 
            elif num >= 100 and num < 400: 
                x += r[100]
                num -= 100 
            elif num >= 500 and num < 1000: 
                x += r[500]
                num -= 500 
            elif num >= 1000:
                x += r[1000]
                num -= 1000
        return x 