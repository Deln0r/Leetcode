class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        ans = ''
        left = '.'
        dots = 0

        for domino in dominoes:
            if domino == '.':
                dots += 1
            else:
                if dots == 0:
                    ans += domino
                    left = domino
                else:
                    if left in ('.', 'L') and domino == 'L':
                        ans += 'L' * (dots + 1)
                    elif left == '.' and domino == 'R':
                        ans += '.' * dots + 'R'
                    elif left == 'R' and domino == 'R':
                        ans += 'R' * (dots + 1)
                    elif left == 'L' and domino == 'R':
                        ans += '.' * dots + 'R'
                    else: #RL
                        mid = dots % 2
                        half = dots // 2
                        ans += 'R' * half + '.' * mid + 'L' * (half + 1)
                    
                    dots = 0
                    left = domino
        if dots > 0:
            if left == 'L':
                ans += '.' * dots
            elif left == 'R':
                ans += 'R' * dots
            else:
                ans += '.' * dots

        return ans