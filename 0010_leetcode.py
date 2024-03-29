class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p = re.sub('\*+','*',p)
        for item in re.findall(p,s):
            if item == s:
                return True
            else:
                return False