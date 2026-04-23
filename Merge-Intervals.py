1class Solution:
2    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
3        intervals.sort(key = lambda x : x[0])
4        merged = [intervals[0]]
5        for ci in intervals[1:]:
6            le = merged[-1]
7            if ci[0]<=le[1]:
8                le[1] = max(le[1] , ci[1])
9            else:
10                merged.append(ci)
11        return merged