class Solution:
    def invert(self,s):
        return "".join('1' if i=='0' else '0' for i in s)
    def Sn(self,n):
        if n==1:
            return "0"
        Sn_1=self.Sn(n-1)
        return Sn_1+"1"+self.invert(Sn_1)[::-1]
    def findKthBit(self, n: int, k: int) -> str:
        sn=self.Sn(n)
        return sn[k-1]