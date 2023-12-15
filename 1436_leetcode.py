class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        starts = {i[0] for i in paths}

        for i in paths:
            if i[1] not in starts:
                starts.clear()
                paths.clear()
                return i[1]
