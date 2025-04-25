class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        ans, pref, dic = 0, 0, defaultdict(int)
        dic[0] = 1
        for num in nums:
            if num % modulo == k:
                pref += 1
            ans += dic[(pref - k) % modulo]
            dic[pref % modulo] += 1
        return ans