class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        students.sort()
        seats.sort()
        count=0
        for i in range(len(students)):
            if students[i]!=seats[i]:
                count+=abs(students[i]-seats[i])
        return count