class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        for row in box: #Check right to left
            start = len(row) - 1
            for i in range(len(row)-1, -1, -1):
                if row[i] == "*": #Obstacle
                    start = i - 1
                elif row[i] == "#": #Stone
                    row[start], row[i] = row[i], row[start]
                    start -= 1

        result = zip(*box[::-1])
        return result