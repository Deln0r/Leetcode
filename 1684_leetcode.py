class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        all_set = set(allowed)
        counter = 0
        for i in words:
            flag = True
            for j in i:
                if j not in all_set:
                    flag = False
                    break
            if flag:
                counter += 1
        return counter


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        all_set = set(allowed)
        counter = 0
        for i in words:
            counter += 0 if len(set(i)-all_set) else 1
        return counter