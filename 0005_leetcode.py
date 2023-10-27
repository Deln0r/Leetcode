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