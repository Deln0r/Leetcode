class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        ans = 0
        for i in s:
            if i == "(":
                stack.append(i)
            elif len(stack)>0 and i == ")":
                stack.pop()
            elif i == ")":
                ans += 1
        return len(stack) + ans