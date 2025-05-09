        nums = list(map(int, num))
        counter = Counter(nums)
        summ = sum(nums)
        if summ % 2:
            return 0
        target = summ // 2
        n = len(nums)

        @cache
        def dfs(i, target, odd_left, even_left) -> int:
            if i > 9:
                if target == 0 and odd_left ==0 and even_left == 0:
                    return 1
                else:
                    return 0
            if odd_left == 0:
                if target != 0:
                    return 0
            res = 0
            for odd_spend in range(min(counter[i], odd_left)+1):
                even_spend = counter[i] - odd_spend
                if odd_spend*i > target or even_spend > even_left: continue
                num_perm = (math.comb(odd_left, odd_spend) * math.comb(even_left, even_spend) * dfs(
                    i+1, target-odd_spend*i, odd_left-odd_spend, even_left-even_spend
                )) % MOD
                res = (res + num_perm) % MOD
            return res

        MOD = 10**9 + 7

        return dfs(0, target, n//2, (n+1)//2)