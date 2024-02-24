class Solution:
    def myAtoi(self, s: str) -> int:
     
        if not s:
            return 0
        sign = 1
        integer = 0
        i = 0
        while i < len(s) and s[i] == ' ':
            i+=1    #skipping leading white space
        if i < len(s) and (s[i] == '-' or s[i] == '+'):
            if s[i] == '-':
                sign = -1
            i+=1
        while(i < len(s) and s[i].isdigit()):
            integer = integer * 10 + int(s[i])
            i+=1
            
        integer = sign*integer
        ans = self.limit(integer)
        return ans
    
    def limit(self, num):
        if num > pow(2, 31) -1:
            return pow(2, 31) -1
        if num < -1*pow(2, 31):
            return -1*pow(2, 31)
        return num
