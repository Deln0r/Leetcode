class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        cache={}
        def count(i,k,prev,prev_cnt):
            if (i,k,prev,prev_cnt) in cache:
                return cache[(i,k,prev,prev_cnt)]
            if k<0:
                return float("inf")
            if i==len(s):
                return 0
            if s[i] == prev :
                incr = 1 if prev_cnt in [1,9,99] else 0
                res = incr + count(i+1,k,prev,prev_cnt+1)
            else:
                res=min(
                    count(i+1,k-1,prev,prev_cnt),
                    1+count(i+1,k,s[i],1)
                )
            cache[(i,k,prev,prev_cnt)]=res
            return res
        return count(0,k,"",0)
