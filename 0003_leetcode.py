class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp =""
        ans = ""
        for i in s:
            if i not in temp:
                temp += i
            else:
                ind = temp.index(i)
                ans = temp if len(temp)>len(ans) else ans
                temp = temp[ind + 1:]
                temp += i
        ans = temp if len(temp) > len(ans) else ans        

        return len(ans)
