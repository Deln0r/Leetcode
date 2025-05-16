class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        f_map = {}
        from_ = [0] * n
        global_max_f = max_i = 0
        for i in range(n - 1, -1, -1):
            w, g = words[i], groups[i]
            hash_val = sum((ord(b) & 31) << (j * 6) for j, b in enumerate(w))

            f = 0
            for j in range(len(w)):
                h = hash_val | (31 << (j * 6))
                max_f, idx, max_f2, idx2 = f_map.get(h, (0, 0, 0, 0))
                if g != groups[idx]:
                    if max_f > f:
                        f = max_f
                        from_[i] = idx
                else:
                    if max_f2 > f:
                        f = max_f2
                        from_[i] = idx2

            f += 1
            if f > global_max_f:
                global_max_f, max_i = f, i

            for j in range(len(w)):
                h = hash_val | (31 << (j * 6))
                max_f, idx, max_f2, idx2 = f_map.get(h, (0, 0, 0, 0))
                if f > max_f:
                    if g != groups[idx]:
                        max_f2, idx2 = max_f, idx
                    max_f, idx = f, i
                elif f > max_f2 and g != groups[idx]:
                    max_f2, idx2 = f, i
                f_map[h] = (max_f, idx, max_f2, idx2)

        ans = [''] * global_max_f
        i = max_i
        for k in range(global_max_f):
            ans[k] = words[i]
            i = from_[i]
        return ans