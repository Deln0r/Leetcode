class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        left = 0

        for c in s:
            if c=='(':
                left+=1
                stack.append('(')
            elif c==')':
                if left == 0:
                    continue
                left-=1
                stack.append(')')
            else:
                stack.append(c)

        ans = ''
        while stack:
            c = stack.pop()
            if c=='(' and left>0:
                left-=1
                continue
            ans+=c

        return ans[::-1]