1class Solution:
2    def threeSum(self, nums: list[int]) -> list[list[int]]:
3        res =set()
4        nums.sort()
5        for i in range(len(nums)-2):
6            start , end = i+1 , len(nums)-1
7            while(start<end):
8                tsum = nums[start]+nums[end] + nums[i]
9                if(tsum ==0):
10                    res.add((nums[start] , nums[end] , nums[i]))
11                    start+=1
12                    end-=1
13                elif(tsum<0):
14                    start+=1
15                else:
16                    end-=1
17        return [list(i) for i in res]