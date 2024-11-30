class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        degree = defaultdict(int)

        for s, e in pairs:
            graph[s].append(e)
            degree[s] += 1
            degree[e] -= 1
        
        root = pairs[0][0]
        for s, e in pairs:
            if degree[s] == 1:
                root = s
    

        res = []

        def dfs(root):
            while graph[root]:
                child = graph[root].pop()
                dfs(child)
                res.append([root, child])
        
        dfs(root)


        return res[::-1]