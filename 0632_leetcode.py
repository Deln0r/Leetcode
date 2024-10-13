class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:

        # the first step 
        # -v.pop() for each maximum   
        choice = [(-v.pop(),i) for i, v in enumerate(nums)]
        lower = -max(choice)[0] #the lower bound
        heapq.heapify(choice)
        
        # compare
        def smaller(int1, int2):
            if int1[1] - int1[0] < int2[1] - int2[0]:
                return int1
            elif int1[1] - int1[0] == int2[1] - int2[0] and int1[0] < int2[0]:
                return int1
            
            return int2


        smallest = [-float('inf'),float(inf)]
        while 1:
            current, i = heapq.heappop(choice)
            current *= -1
            smallest = smaller(smallest,[lower,current])

            if not nums[i]:
                return smallest

            nxt = nums[i].pop()
            lower = min(nxt,lower) #update the lower bound
            heapq.heappush(choice,(-nxt,i))

        return   