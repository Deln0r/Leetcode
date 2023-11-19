class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        cnt=Counter(nums)
        lst=list(cnt.keys())
        lst.sort()
        sm=0
        for i in range(len(lst)):
            sm+=(i*cnt[lst[i]])

        return sm
