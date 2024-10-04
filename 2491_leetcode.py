class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i=0
        j=len(skill)-1
        prev=skill[i]+skill[j]
        sum=skill[i]*skill[j]
        i+=1
        j-=1
        while(i<j):
            if (skill[i]+skill[j])!=prev:
                return -1
            else:
                sum+=skill[i]*skill[j]
            i+=1
            j-=1
        return sum