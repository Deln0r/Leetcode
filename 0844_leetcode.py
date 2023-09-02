class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def typing(s):
            stack = []
            for i in s:
                if i == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(i)
            return str(stack)
        return typing(s) == typing(t)
