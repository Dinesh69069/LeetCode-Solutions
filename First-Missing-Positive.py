1class Solution:
2    def firstMissingPositive(self, nums: List[int]) -> int:
3        n = len(nums)
4        i = 0
5        while(i<n):
6            correct_index = nums[i]-1
7            if(0 < nums[i] <= n and nums[i] != nums[correct_index]):
8                nums[i] , nums[correct_index] = nums[correct_index] , nums[i]
9            else:
10                i+=1
11        for i in range(n):
12            if(nums[i] != i+1):
13                return i+1
14        return n+1