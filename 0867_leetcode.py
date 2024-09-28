class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        l=[]
        for i in range(len(matrix[0])):
            temp = []
            for j in range(len(matrix)):
                temp.append(matrix[j][i])
            l.append(temp)
        return l
    

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])

        ans = []

        for r in range(cols):
            row = []
            for c in range(rows):
                row.append(matrix[c][r])
            ans.append(row)
        return ans
