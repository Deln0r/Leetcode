class Solution:
    def smallestNumber(self, p: str) -> str:
        i = 0
        d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        s = ""
        while i < len(p):
            if p[i] == "D":
                k = i
                c = 0
                while k < len(p) and p[k] == "D":
                    k += 1
                    c += 1
                for j in range(c, -1, -1):
                    s += str(d.pop(j))
                    i += 1
            else:
                s += str(d.pop(0))
                i += 1
        if p[-1] == "I":
            s += str(d.pop(0))
        return s