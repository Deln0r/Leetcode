class Solution:
    def digitCount(self, num: str) -> bool:
        for i in range(len(num)):
            if str(num[i]) != str(num.count(str(i))):
                return False
        return True

class Solution:
    def digitCount(self, num: str) -> bool:
        counter = Counter(num)
        for i in range(len(num)):
            if num[i] != str(counter[str(i)]):
                return False
        return True