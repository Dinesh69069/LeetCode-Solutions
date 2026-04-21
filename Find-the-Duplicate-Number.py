1class Solution:
2    def findDuplicate(self, nums: List[int]) -> int:
3        fast = slow = nums[0]
4        while(fast!=len(nums)):
5            slow = nums[slow]
6            fast = nums[nums[fast]]
7            if(slow ==fast):
8                fast = nums[0]
9                while(fast != slow):
10                    slow = nums[slow]
11                    fast = nums[fast]
12                return fast