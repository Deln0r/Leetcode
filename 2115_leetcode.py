class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        res = []
        for i,v in zip(recipes,ingredients):
            graph[i] = v

        visit = set(supplies)

        def getRecipes(graph, curr, repeat):
            if curr in repeat or curr not in graph:
                return False
            repeat.add(curr)
            for i in graph[curr]:
                if i not in visit:
                    if getRecipes(graph, i,repeat):
                        visit.add(i)
                    else:
                        return False
                    
            return True
        
        for i in recipes:
            if i not in visit:
                if getRecipes(graph,i, set()):
                    visit.add(i)
                    res.append(i)
            else:
                res.append(i)


        return res