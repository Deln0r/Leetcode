class Solution:
    def peakIndexInMountainArray(self, arr):
        left, r = 0, len(arr) - 1
        while left <= r:
            mid = (left + r) // 2
            if arr[mid - 1] < arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid] > arr[mid - 1]:
                left = mid
            else:
                r = mid
