class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def centre(edges):
            n=len(edges)+1
            degree = [0]*n
            leaves=[]
            map = collections.defaultdict(list)
            for u,v in edges:
                map[u].append(v)
                map[v].append(u)
                degree[u]+=1
                degree[v]+=1
            for i in range(n):
                if degree[i]<=1:
                    leaves.append(i)
            count=len(leaves)
            j=0
            while count<n:
                new_leaves=[]
                for l in leaves:
                    for nei in map[l]:
                        degree[nei]-=1
                        if degree[nei]==1:
                            new_leaves.append(nei)
                    degree[l]=0
                leaves=new_leaves
                count+=len(leaves)
                j+=2
            h = j//2 +(len(leaves)-1)
            j+= (len(leaves)-1)
            return h,j
        h1,d1 = centre(edges1)
        h2,d2 = centre(edges2)
        return max(h1+h2+1,max(d1,d2))
            
        

