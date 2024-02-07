class Solution:
    def frequencySort(self, s: str) -> str:
        freqHashMap = Counter(s)
        sortingList = [""] * len(s)
        for key, value in freqHashMap.items():
            sortingList[value-1] += key*value
        result = ''.join(sortingList[::-1])
        return result