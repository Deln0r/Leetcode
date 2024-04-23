class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:    
        visit = set(deadends)
        if '0000' in deadends:
            return -1
            
        q = deque()
        q.append(('0000',0))

        while q :
            lock, step = q.popleft()
            if lock == target:
                return step
            
            for i in range(4):
                for num in [1,-1]:
                    digit = str((int(lock[i]) + num + 10) % 10) 
                    lock_num = lock[:i] + digit + lock[i+1:]
                    if lock_num not in visit:
                        visit.add(lock_num)
                        q.append((lock_num, step+1))
        
        return -1