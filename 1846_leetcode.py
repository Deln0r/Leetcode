class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        ind, maxx = 0, 0
        while ind < len(arr):
            if arr[ind] > maxx: maxx += 1; ind += 1
            else: ind = bisect_right(arr, maxx, lo=ind)
        return maxx
