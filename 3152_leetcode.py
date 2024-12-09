class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        special=[]
        count=0
        for i in range(len(nums)):
            if i==0:
                special.append(count)
            elif nums[i-1]%2==0 and nums[i]%2==0:
                count+=1
                special.append(count)
            elif nums[i-1]%2==1 and nums[i]%2==1:
                count+=1
                special.append(count)
            else:
                special.append(count)

        result=[]

        for query in queries:
            if special[query[1]]-special[query[0]]>0:
                result.append(False)
            else:
                result.append(True)
        
        return result