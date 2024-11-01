class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = []
        counter = 0
        temp = ''
        for i in s:
            if temp == i and counter < 2:
                ans.append(i)
                counter += 1
            elif temp == i and counter > 2:
                continue
            elif temp != i:
                ans.append(i)
                temp = i
                counter = 1
        return ''.join(ans)