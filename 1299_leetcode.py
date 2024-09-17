class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        m = max(arr)
        for i in range(len(arr)-1):
            if arr[i] < m:
                arr[i] = m
            else:
                m = max(arr[i+1:])
                arr[i] = m
        arr[-1] = -1
        return arr

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_ = -1
        for i in range(len(arr)-1, -1, -1):
            temp = arr[i]
            arr[i] = max_
            max_ = max(max_, temp)
        return arr