import bisect
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        n = len(items)
        high = items[0][1]
        result = [high]
        for i in range(1, n):
            high = max(high, items[i][1])
            result.append(high)
        print(result, items)
        ans = []
        for cost in queries:
            index = bisect.bisect_right(items, [cost, 1000000000])
            if index == 0:
                ans.append(0)
            else:
                ans.append(result[index - 1])
        return ans