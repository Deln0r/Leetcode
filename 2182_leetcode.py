class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        count = collections.Counter(s)
        heap=[]
        for k,v in count.items():
            heap.append([k,v])
        heap.sort()
        n=len(s)
        j=len(heap)-1
        res=[]
        for i in range(n):
            if j<0:
                break
            k=j-1
            r,ind=0,0
            while ind<heap[j][1]:
                if r<repeatLimit:
                    r+=1
                    ind+=1
                    res.append(heap[j][0])
                    continue
                if heap[k][1]==0:
                    k-=1
                if k<0:
                    break
                heap[k][1]-=1
                res.append(heap[k][0])
                r=0
            j-=1
        return ''.join(res)