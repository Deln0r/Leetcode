class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        freq = [0,0,0,0,0,0,0,0,0,0]
        ans = []

        for i in digits:
            freq[i]+=1
        
        for i in range(100,1000):
            temp = [0] * 10
            x=i
            while x>0:
                temp[x%10] += 1
                x=x//10
            if all(temp[d] <= freq[d] for d in range(10)):
                if i%2 == 0:
                    ans.append(i)
        return ans