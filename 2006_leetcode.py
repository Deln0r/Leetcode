class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        ans = 0
        db = Counter()

        for num in nums:
            pair1 = num + k
            pair2 = num - k
            ans += db[pair1]
            ans += db[pair2]
            db[num] += 1
        return ans