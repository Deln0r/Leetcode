class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        size=[]
        lastind={char:ind for ind,char in enumerate(s)}
        left=0
        right=0
        shift=0
        for left in range(len(s)):
            right=max(right,lastind[s[left]])
            if left==right:
                size.append(left+1-shift)
                shift=left+1
        return size