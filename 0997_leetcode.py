class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n==1 and trust==[]:
            return 1
        a = set()
        b = set()
        d = {}
        for i in trust:
            if i[1] not in d:
                d[i[1]] = set()
                d[i[1]].add(i[0])
            else:
                d[i[1]].add(i[0])
            a.add(i[0])
            b.add(i[1])
        t = b.union(a)
        if len(t)==0:
            return -1
        for i in t:
            if d.get(i) is not None:
                if len(d[i]) == n - 1:
                    if i not in a:
                        return i
        return -1