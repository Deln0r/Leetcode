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
