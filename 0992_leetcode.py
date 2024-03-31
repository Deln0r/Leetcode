class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def remove_element(el):
            if dct[el] == 1:
                del dct[el]
            else:
                dct[el] -= 1
        
        ans = [0, 0]
        for loop, kk in enumerate((k, k-1)):
            l = r = 0
            dct = {}
            for r in range(len(nums)):
                dct[nums[r]] = dct.get(nums[r], 0) + 1
                ans[loop] += r - l

                if len(dct) <= kk:
                    continue

                while len(dct) > kk:
                    remove_element(nums[l])
                    l += 1

            ans[loop] += r - l + 1

        return sub(*ans)