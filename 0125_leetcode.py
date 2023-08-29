class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''
        for i in s.lower():
            if i.isalpha() or i.isnumeric():
                string += i
        return string == string[::-1]


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, r = 0, len(s) - 1
        while left <= r:
            if not s[l].isalnum():
                left += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            if s[left].lower() != s[r].lower():
                return False
            left += 1
            r -= 1
        return True
