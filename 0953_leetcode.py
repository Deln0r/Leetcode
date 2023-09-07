class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        sorted_list = list(sorted(words,key = lambda word:[order.index(i) for i in word]))
        return words == sorted_list
