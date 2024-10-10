class Solution:
    def interpret(self, command: str) -> str:
        return command.replace('()', 'o').replace('(al)', 'al')
    
    
class Solution:
    def interpret(self, command: str) -> str:
        ans = ''
        temp = ''

        for c in command:
            temp += c

            if temp == 'G':
                ans += 'G'
                temp = ''
            elif temp == '()':
                ans += 'o'
                temp = ''
            elif temp == '(al)':
                ans += 'al'
                temp = ''
        return ans