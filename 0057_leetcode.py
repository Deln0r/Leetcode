class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        list1=[]
        for i in range(len(intervals)):
            if newInterval[1]<intervals[i][0]:
                list1.append(newInterval)
                return list1+intervals[i:]
            elif newInterval[0]>intervals[i][1]:
                list1.append(intervals[i])
            else:
                newInterval=[min(newInterval[0],intervals[i][0]),max(intervals[i][1],newInterval[1])]
        list1.append(newInterval)
        return list1