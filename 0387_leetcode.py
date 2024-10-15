class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        return min([i for i in range(len(s)) if c[s[i]] == 1], default = -1)
    

class Solution:
    def firstUniqChar(self, s: str) -> int:
        my_dict = {}
        for i in s:
            if i in my_dict:
                my_dict[i] += 1
            else:
                my_dict[i] = 1
        
        for i in range(len(s)):
            if my_dict[s[i]] == 1:
                return i
        return -1