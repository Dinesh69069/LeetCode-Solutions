1class Solution:
2    def twoSum(self, numbers: List[int], target: int) -> List[int]:
3        start  , end = 0 , len(numbers)-1
4        while(start < end):
5            if(numbers[start]+numbers[end] == target):
6                return [start +1 , end+1]
7            elif(numbers[start]+numbers[end] < target):
8                start+=1
9            else:
10                end-=1