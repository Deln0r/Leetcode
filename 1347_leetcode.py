class Solution:
    def minSteps(self, s: str, t: str) -> int:
        return sum((Counter(t)-Counter(s)).values())


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s, count_t = Counter(s), Counter(t)
        res = 0
        
        for  k, v in count_s.items():
            num = count_t.get(k)
            
            if num is None: res += v
            elif num < v:   res += (v - num)

        return res