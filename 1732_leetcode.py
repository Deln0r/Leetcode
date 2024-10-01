class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        arr = [0]
        for i in range(len(gain)):
            point = arr[i] + gain[i]
            arr.append(point)
        return max(arr)
    

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0
        cur = 0
        for g in gain:
            cur += g
            ans = max(ans, cur)
        return ans