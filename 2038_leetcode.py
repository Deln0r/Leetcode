class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        c = 0

        for i in range(1, len(colors)-1):
            if colors[i-1]=="A" and colors[i]=="A" and colors[i+1]=="A":
                c +=1
            elif colors[i-1]=="B" and colors[i]=="B" and colors[i+1]=="B":
                c -= 1

        if c>0:
            return True
        return False
