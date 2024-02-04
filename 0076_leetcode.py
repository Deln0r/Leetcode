class Solution(object):
    def minWindow(self, s, t):
        m, n = len(s), len(t)
        mp = {}

        ans = float('inf')
        start = 0

        for x in t:
            mp[x] = mp.get(x, 0) + 1

        count = len(mp)

        i = 0
        j = 0

        while j < len(s):
            mp[s[j]] = mp.get(s[j], 0) - 1
            if mp[s[j]] == 0:
                count -= 1

            if count == 0:
                while count == 0:
                    if ans > j - i + 1:
                        ans = j - i + 1
                        start = i
                    mp[s[i]] = mp.get(s[i], 0) + 1
                    if mp[s[i]] > 0:
                        count += 1

                    i += 1
            j += 1

        if ans != float('inf'):
            return s[start:start + ans]
        else:
            return ""