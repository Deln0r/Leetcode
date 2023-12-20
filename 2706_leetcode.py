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
