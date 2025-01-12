class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False
        star_stack = []
        open_stack = []
        for i in range(len(s)):
            if locked[i] == "0":
                star_stack.append(i)
            elif s[i] == "(":
                open_stack.append(i)
            else:
                if open_stack:
                    open_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False

        while open_stack and star_stack and open_stack[-1] < star_stack[-1]:
            open_stack.pop()
            star_stack.pop()
        return not bool(len(open_stack))
