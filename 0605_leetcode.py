class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
        return n <= 0

# 17.09.2024
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        counter = 0
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i-1] + flowerbed[i] + flowerbed[i+1] == 0:
                flowerbed[i] = 1
                counter += 1

        return counter >= n
