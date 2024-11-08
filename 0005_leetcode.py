class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            left = i;right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:left -= 1;right += 1
            palindrome = s[left+1:right]
            if len(palindrome) > len(longest):longest = palindrome
            left = i;right = i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:left -= 1;right += 1
            palindrome = s[left+1:right]  
            if len(palindrome) > len(longest):longest = palindrome
        return longest

class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""

        for i in range(len(s)):
            l, r = i, i

            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if len(s[l:r+1]) > len(ans):
                        ans = s[l:r+1]
                    l-=1
                    r+=1
                else:
                    break

            l, r = i, i+1
            
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if len(s[l:r+1]) > len(ans):
                        ans = s[l:r+1]
                    l-=1
                    r+=1
                else:
                    break
        return ans