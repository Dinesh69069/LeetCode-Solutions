1class Solution:
2    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
3        i = 0
4        n = len(nums)
5        while(i<n):
6            correct_index = nums[i] - 1
7            if(nums[i] != nums[correct_index]):
8                nums[i] , nums[correct_index]  = nums[correct_index] , nums[i]
9            else:
10                i+=1
11        print(nums)
12        res = []
13        for i in range(n):
14            if(nums[i]!= i+1):
15                res.append(i+1)
16        return res