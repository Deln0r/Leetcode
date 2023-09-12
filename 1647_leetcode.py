class Solution(object):
    def minDeletions(self, s):
        char_count = Counter(s)
        deletions = 0
        unique_frequencies = set()
        for char, freq in char_count.items():
            while freq > 0 and freq in unique_frequencies:
                freq -= 1
                deletions += 1
            unique_frequencies.add(freq)
        return deletions
