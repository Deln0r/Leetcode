class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        stars = []
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == '*':
                stars.append(i)
            else:
                if stack:
                    stack.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
        
        while stack and stars:
            if stack[-1] < stars[-1]:
                stack.pop()
                stars.pop()
            else:
                break
        
        return len(stack) == 0