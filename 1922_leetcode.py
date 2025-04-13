class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # Solution 1: First thought, ignoring mod(result, 10**9 + 7)
        # return 20**(n // 2) if n % 2 == 0 else 5*20**(n // 2) 

        # Solution 2: Solution 1 cleaned up
        return (pow(5, (n+1)//2, 10**9+7) * pow(4, n//2, 10**9+7)) % (10**9+7)

        # Solution 3: Easier to read version of Solution 2
        mod = 10**9 + 7
        evens = (n + 1) // 2  # number of even indices (0-indexed)
        odds = n // 2         # number of odd indices
        return (pow(5, evens, mod) * pow(4, odds, mod)) % mod