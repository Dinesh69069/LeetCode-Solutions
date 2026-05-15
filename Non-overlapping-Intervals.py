1class Solution:
2    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
3        intervals.sort(key =lambda x : x[1])
4        target = 0 
5        temp = intervals[0][1]
6        print(intervals)
7        for i in intervals[1:]:
8            if(i[0]<temp):
9                target+=1
10            else:
11                temp = i[1]
12        return target