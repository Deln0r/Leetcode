class Solution:
    def maximumLength(self, s: str) -> int:
        last = s[0]
        cnt = 0
        d = defaultdict(list)

        for c in s:
            if c == last:
                cnt += 1
            else:
                cnt = 1
                last = c
            heapq.heappush(d[last], cnt)
            if len(d[last]) > 3:
                heapq.heappop(d[last])

        ans = -1
        for listFreq in d.values():
            if len(listFreq) < 3:
                continue
            ans = max(ans, min(listFreq))
        return ans