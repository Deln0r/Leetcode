class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:

        numCnt, ctr, ans, idx = len(set(nums)), Counter(), 0, 0

        for rght in nums:
            ctr[rght] += 1

            while len(ctr) == numCnt:
                ctr[(left:= nums[idx])] -= 1
                if ctr[left] == 0: del ctr[left]

                idx+= 1

            ans+= idx

        return ans