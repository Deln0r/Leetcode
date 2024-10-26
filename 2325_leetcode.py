class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        d = {' ': ' '}
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        counter = 0

        for i, k in enumerate(key):
            if k == ' ' or k in d:
                continue
            else:
                d[k] = alphabet[counter]
                counter += 1
        
        ans = []
        for m in message:
            ans.append(d[m])
        return ''.join(ans)
