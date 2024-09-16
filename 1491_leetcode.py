class Solution:
    def average(self, salary: List[int]) -> float:
        total = 0
        mi = float('inf')
        ma = float('-inf')

        for s in salary:
            total += s
            mi = min(s, mi)
            ma = max(s, ma)
        
        total = total - mi - ma
        avg = total / (len(salary) - 2)
        return avg