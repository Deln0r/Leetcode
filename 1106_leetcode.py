class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        operands=deque()
        operators=deque()
        for i in expression:
            if i=='&' or i=='|' or i=='!':
                operators.append(i)
            elif i==')':
                operator=operators.pop()
                s=''
                while operands[-1]!='(':
                    s+=operands.pop()
                    print(s)
                operands.pop()
                if operator=='&':
                    if 'f' in s:
                        operands.append('f')
                    else:
                        operands.append('t')
                elif operator=='|':
                    if 't' in s:
                        operands.append('t')
                    else:
                        operands.append('f')
                elif operator=='!':
                    if s=='t':
                        operands.append('f')
                    else:
                        operands.append('t')
            elif i=='t' or i=='f' or i=='(':
                operands.append(i)
        print(operators,operands)
        return True if operands[0]=='t' else False