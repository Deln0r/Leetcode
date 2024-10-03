class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        n = sum(apple)
        c = 0

        capacity.sort(reverse=True)

        for i in range(len(capacity)):
            c += capacity[i]
            if c >= n:
                return i+1