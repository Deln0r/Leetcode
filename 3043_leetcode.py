class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        X, Y = len(arr1), len(arr2)

        s = set()
        for i in arr2:
            copy = i
            # 12345 -> 1, 12, 123, 1234, 12345
            s.add(copy)
            copy = copy // 10
            while copy > 0:
                s.add(copy)
                copy = copy // 10
        
        t = set()
        for i in arr1:
            copy = i
            # 12345 -> 1, 12, 123, 1234, 12345
            t.add(copy)
            copy = copy // 10
            while copy > 0:
                t.add(copy)
                copy = copy // 10
                
        ans = 0
        for i in t:
            if i in s:
                ans = max(ans, len(str(i)))
                
        return ans