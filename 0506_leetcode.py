class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sc=sorted(score,reverse=True)
        mapping={}
        for i in range(len(sc)):
            if i==0:
                mapping[sc[i]]="Gold Medal"
            elif i==1:
                mapping[sc[i]]="Silver Medal"
            elif i==2:
                mapping[sc[i]]="Bronze Medal"
            else:
                mapping[sc[i]]=str(i+1)
        res=[]
        for i in score:
            res.append(mapping[i])
        return res