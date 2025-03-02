class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        d={}
        for i in nums1:
            id,val = i
            if id in d:
                d[id]+=val
            else:
                d[id] = val
        for i in nums2:
            id,val = i
            if id in d:
                d[id]+=val
            else:
                d[id] = val
        ans=[[a,b]for a,b in d.items()]
        ans.sort(key=lambda x:x[0])
        return ans