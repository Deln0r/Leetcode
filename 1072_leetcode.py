class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        """
        1. 2 rows can be equalized if they share the same finger print.
        2. First value in the row is assigned T and the next values are assigned T if equal to first else F.
        3. If the fingerprint matches then they can be equalized as after reverting all F they can be converted to T thereby equalizing to first element.
        """
        #Default dict for storing the finger print of each row
        d=defaultdict(int)

        m=len(matrix)
        n=len(matrix[0])
        res=0
        for i in range(m):
            s="T"
            f=matrix[i][0]
            for j in range(1,n):
                if matrix[i][j]==f:
                    s+="T"
                else:
                    s+="F"
            d[s]+=1
            res=max(res,d[s])
        return res