class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        ans = 0

        for c in s:
            if c=='(':
                stack.append(c)
            elif c==')':
                if not stack:
                    return ans
                stack.pop()
            else:
                continue
            ans = max(ans,len(stack))

        return ans