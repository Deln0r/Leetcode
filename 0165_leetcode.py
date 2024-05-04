class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1=version1.split('.')
        ver2=version2.split('.')
        i=0
        maxlen=max(len(ver1),len(ver2))
        while i<maxlen:
            v1=int(ver1[i]) if i<len(ver1) else 0
            v2=int(ver2[i]) if i<len(ver2) else 0
            if v1<v2:
                return -1
            elif v1>v2:
                return 1
            else:
                i+=1
        return 0