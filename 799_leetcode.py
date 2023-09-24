class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        glasses=[poured]
        for i in range(query_row):
            temp=[0]*(len(glasses)+1)
            for i in range(len(glasses)):
                pour=max(0,glasses[i]-1)/2
                temp[i]+=pour
                temp[i+1]+=pour
            glasses=temp
        return min(1,glasses[query_glass])
