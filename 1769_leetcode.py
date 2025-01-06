class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        bl, br = 0, 0
        ml, mr = 0, 0
        n = len(boxes)
        res = [0]*n
        for i in range(n):
            res[i] += bl + ml
            j = n-1-i
            res[j] += br + mr
            ml = bl + ml
            mr = br + mr
            bl += 1 if boxes[i] == '1' else 0
            br += 1 if boxes[j] == '1' else 0
            # print(res, i)
        return res
