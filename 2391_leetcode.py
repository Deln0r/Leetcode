class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        travel_time , s = [] , 0 
        lis=''.join(garbage)
        d = Counter(lis)
        for i in range(1,len(garbage)):
            s += travel[i-1]
            travel_time.append(s)
        last_index = defaultdict(int)
        for i in range(len(garbage)):
            if 'M' in garbage[i]:
                last_index['M'] = i
            if 'P' in garbage[i]:
                last_index['P'] = i
            if 'G' in garbage[i]:
                last_index['G'] = i
        ans = 0
        for i in d:
            ans += d[i]
            if last_index[i] > 0 :  ans += travel_time[last_index[i] - 1]
        return ans
