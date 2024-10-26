class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        counter = Counter(nums)
        max_freq = 0
        ans = -1

        for k, v in counter.items():
            if k % 2 == 0:
                if v > max_freq or (v == max_freq and k < ans):
                    ans = k
                    max_freq = v
        return ans