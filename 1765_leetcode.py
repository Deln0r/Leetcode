class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        result = [[0 for _ in range(n)] for _ in range(m)]
        queue = []
        for i in range(m): 
            for j in range(n): 
                if isWater[i][j]: queue.append((i, j))

        height = 1 
        while queue: 
            new_queue = []
            for i, j in queue: 
                for inc in [-1, 1]: 
                    ni, nj = i + inc, j + inc 
                    if 0 <= ni < m and not isWater[ni][j] and result[ni][j] == 0: 
                        result[ni][j] = height 
                        new_queue.append((ni, j))
                    if 0 <= nj < n and not isWater[i][nj] and result[i][nj] == 0: 
                        result[i][nj] = height 
                        new_queue.append((i, nj))
            queue = new_queue 
            height += 1 
        return result 