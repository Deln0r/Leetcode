class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        def prime_score(num):
            res = 0
            if num % 2 == 0:
                res = 1
                num //= 2
                while num >= 2 and num % 2 == 0:
                    num //= 2
            d = 3
            while num >= d * d:
                if num % d == 0:
                    res += 1
                    num //= d
                    while num >= d and num % d == 0:
                        num //= d
                d += 2
            return res if num < d else res + 1

        mod = 1000000007
        n = len(nums)
        order = sorted(range(n), key = lambda i: -nums[i])
        arr_prime_score = [0] * n
        memo = {}
        for i, num in enumerate(nums):
            if num in memo:
                arr_prime_score[i] = memo[num]
            else:
                arr_prime_score[i] = prime_score(num)
                memo[num] = arr_prime_score[i]
        max_score = 1
        right = [0] * n
        stack = []
        for i, score in enumerate(arr_prime_score):
            while stack and score > arr_prime_score[stack[-1]]:
                right[stack.pop()] = i - 1
            stack.append(i)          
        while stack:
            right[stack.pop()] = n-1
        left = [0] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and arr_prime_score[i] >= arr_prime_score[stack[-1]]:
                left[stack.pop()] = i + 1
            stack.append(i)          
        while stack:
            left[stack.pop()] = 0
        cnt_operations = 0
        for j in range(n):
            i = order[j]
            current = (i - left[i] + 1) * (right[i] - i + 1)
            if cnt_operations + current < k:
                max_score = max_score * pow(nums[i], current, mod) % mod
                cnt_operations += current
            else:
                max_score = max_score * pow(nums[i], k - cnt_operations, mod) % mod
                break
        return max_score