# Union-find, Time O(V + E), Space O(V)
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Define parent and rank array
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        # Define find & union
        def find(n):
            if n != par[n]:
                par[n] = find(par[n])
            return par[n]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            # Already connected
            if p1 == p2:
                return False
            # Connect
            if rank[p1] >= rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        # Find redundant edge
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]