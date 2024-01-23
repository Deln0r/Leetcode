class Solution:
    def maxLength(self, arr: List[str]) -> int:
        elem = ['']
        maxim = 0
        for i in range(len(arr)):
            x = len(elem)
            for j in range(x):
                x = arr[i] + elem[j]
                if len(x) == len(set(x)):
                    elem.append(x)
                    maxim = max(maxim,len(x))
        return maxim