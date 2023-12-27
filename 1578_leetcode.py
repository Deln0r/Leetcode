class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        prev=colors[0]
        curr_max = neededTime[0]
        cost = 0
        for i in range(1,len(colors)):
            curr = colors[i]
            if curr == prev :
                if neededTime[i] > curr_max :
                    cost += curr_max
                    curr_max = neededTime[i]
                else :
                    cost += neededTime[i]
            if curr != prev :
                curr_max = neededTime[i]
                prev = colors[i]
        return cost
