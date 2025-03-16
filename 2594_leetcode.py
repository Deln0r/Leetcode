class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left, right = 1, min(ranks) * cars * cars
        ans = 0

        while left <= right:
            mid = left + (right - left) // 2
            count = 0

            for rank in ranks:
                count += math.isqrt(mid // rank)

                if count >= cars:
                    break
                
            if count >= cars:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans