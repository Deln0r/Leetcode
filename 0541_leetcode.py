class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans = ""
        flag = True

        for i in range(0, len(s), k):
            if flag:
                ans += s[i: i+k][::-1]
            else:
                ans += s[i: i+k]
            flag = not flag
        return ans