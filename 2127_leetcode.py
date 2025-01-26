class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        deg = [0] * n
        for f in favorite:
            deg[f] += 1

        max_depth = [1] * n
        q = deque(i for i, d in enumerate(deg) if d == 0)
        while q:
            x = q.popleft()
            y = favorite[x]
            max_depth[y] = max_depth[x] + 1
            deg[y] -= 1
            if deg[y] == 0:
                q.append(y)

        max_ring_size = sum_chain_size = 0
        for i, d in enumerate(deg):
            if d == 0: continue

            deg[i] = 0
            ring_size = 1
            x = favorite[i]
            while x != i:
                deg[x] = 0
                ring_size += 1
                x = favorite[x]

            if ring_size == 2:
                sum_chain_size += max_depth[i] + max_depth[favorite[i]]
            else:
                max_ring_size = max(max_ring_size, ring_size)
        return max(max_ring_size, sum_chain_size)