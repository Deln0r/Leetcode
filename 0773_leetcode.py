moves = ((1,3), (0,2,4), (1,5),
         (0,4), (1,3,5), (2,4))

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:

        state = (*board[0], *board[1])
        queue, seen, cnt = deque([state]), set(), 0

        while queue:

            for _ in range(len(queue)):
                state = list(queue.popleft())
                idx = state.index(0)
                if state == [1,2,3,4,5,0]: return cnt

                for i in moves[idx]:
                    curr = state[:]
                    curr[idx], curr[i] = curr[i], 0
                    curr = tuple(curr)
                    if curr in seen: continue
                    queue.append(curr)
                    seen.add(curr)

            cnt+= 1

        return -1