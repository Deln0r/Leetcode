class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        flowersStartTime = sorted(startTime for startTime, endTime in flowers)
        flowersEndTime = sorted(endTime for startTime, endTime in flowers)
        print(flowersStartTime, flowersEndTime)
        for i in range(len(people)):
            rightIndex =  bisect_right(flowersStartTime, people[i]) 
            leftIndex = bisect_left(flowersEndTime, people[i])
            people[i] = rightIndex - leftIndex

        return people
