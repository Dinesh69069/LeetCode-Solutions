1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        start , end , ma = 0 , len(height)-1 , 0
4        while(start<end):
5            a = min(height[start] , height[end])*(end-start)
6            ma = a if a >ma else ma
7            if(height[start]<height[end]):
8                start+=1
9            else:
10                end-=1
11        return ma