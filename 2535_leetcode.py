class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        count_y = 0
        count_x = 0
        for n in nums:
            if n < 10:
                count_y += n
                count_x += n
            else:
                count_x += n
                temp = n
                while temp:
                    count_y += temp % 10
                    temp = temp // 10
        return abs(count_x - count_y)