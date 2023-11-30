class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        binary = format(n, "b")

        N, res = len(binary), 0
        
        for i in range(1, N+1):
            if binary[-i] == "1": res = 2**i-1 - res
                
        return res