# O(N*N)

# s = 'trytolearnalgoritms'
# ans = ''
# anscnt = 0
# for i in range(len(s)):
#     nowcnt = 0
#     for j in range(len(s)):
#         if s[i] == s[j]:
#             nowcnt += 1
#     if nowcnt > anscnt:
#         ans = s[i]
#         anscnt = nowcnt
# print(ans)
# print(anscnt)

# O(Nk)

# s = 'trytolearnalgoritms'
# ans = ''
# anscnt = 0
# for now in set(s):
#     nowcnt = 0
#     for j in range(len(s)):
#         if now == s[j]:
#             nowcnt += 1
#     if nowcnt > anscnt:
#         ans = now
#         anscnt = nowcnt
# print(ans)
# print(anscnt)

# O(N+k) = O(N)
s = 'trytolearnalgoritms'
ans = ''
anscnt = 0
dct = {}
for now in s:
    if now not in dct:
        dct[now] = 0
    dct[now] += 1
for key in dct:
    if dct[key] > anscnt:
        anscnt = dct[key]
        ans = key
print(ans)
print(anscnt)