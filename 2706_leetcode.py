class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min1 = 99999999
        min2 = 99999999
        for i in prices:
            if min1 > i:
                min2 = min1
                min1=i
            elif min2 > i :
                min2 = i
        if ( min1 + min2 ) > money:
            return money
        else:
            return money - (min1 + min2)


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min1 = float('inf')
        min2 = float('inf')

        for p in prices:
            if p < min1:
                min2, min1 = min1, p
            elif p < min2:
                min2 = p
        ans = money - min1 - min2
        return ans if ans>=0 else money