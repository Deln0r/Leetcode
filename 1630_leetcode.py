class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:

        m = len(l)
        res = []

        for i in range(m):
            passes = True
            left = l[i]
            right = r[i]
            arr = []   
            for j in range(left,right+1):
                arr.append(nums[j])
            arr.sort()

            first,second=0,1
            diff = arr[second]-arr[first]
            while(second < len(arr)):
                if(arr[second] - arr[first] != diff):
                    passes = False
                    break
                first += 1
                second += 1
            if(passes):
                res.append(True)
            else:
                res.append(False)
        
        return res



##################################################### another one
        ans=[True]*len(l)
        
        for i in range(len(l)):
            s=nums[l[i]:r[i]+1]
            s.sort(reverse=True)
            for v in range(len(s)-1):
                if (s[v+1]-s[v])!=(s[1]-s[0]):
                    ans[i]=False
                    break
        return ans