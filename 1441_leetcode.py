class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        i = 0
        ans = []
        cur = 0

        for j in range(1, target[-1] + 1):            
            if target[i] == j:
                while cur and cur - 1 != target[i - 1]:
                    cur -= 1
                    ans.append('Pop')

                i += 1
                cur = j

            ans.append('Push')
            cur += 1

        return ans