class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        signs = {
            '+': lambda x,y: x+y,
            '-': lambda x,y: x-y,
            '*': lambda x,y: x*y,
            '/': lambda x,y: x/y
        }


        for token in tokens:
            if token not in signs:
                stack.append(int(token))
            else:
                right = stack.pop()
                left = stack.pop()
                stack.append(int(signs[token](left, right)))
            
        return stack.pop()
