1class Solution:
2    def compareBitonicSums(self, nums: list[int]) -> int:
3        peak_idx = nums.index(max(nums))
4        ascending_part = nums[:peak_idx+1]
5        descending_part = nums[peak_idx:]
6
7        asc_sum = sum(ascending_part)
8        desc_sum = sum(descending_part)
9        if(asc_sum>desc_sum):
10            return 0
11        elif(asc_sum<desc_sum):
12            return 1
13        else:
14            return -1