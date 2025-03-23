from collections import deque
import heapq
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = (10**9) + 7
     
        adj = [[] for _ in range(n)]
        for src , dst ,timeNeeded in roads:
            adj[src].append((dst ,timeNeeded))
            adj[dst].append((src ,timeNeeded))
        dist = [float('inf')] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1
        pq = []
        heappush(pq ,(0 , 0))
        
        while pq:
            timeTaken , src = heappop(pq)
            
            if timeTaken > dist[n - 1]:
                continue

            for neighbor , timeNeeded in adj[src]:
                totalTime = timeTaken + timeNeeded
                if totalTime < dist[neighbor]:
                    ways[neighbor] = ways[src]
                    dist[neighbor] = totalTime
                    heappush(pq ,(totalTime ,neighbor))
                    
                elif totalTime == dist[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[src]) % MOD

        return ways[n - 1]

        