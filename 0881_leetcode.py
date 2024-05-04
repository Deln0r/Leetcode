class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        c=0
        i=0
        people.sort()
        n=len(people)
        i=0
        j=n-1
        while i<=j:
            if people[i]+people[j]<=limit:
                
                i+=1
                
            j-=1
            c+=1
        return c