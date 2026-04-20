1class Solution:
2    def isHappy(self, n: int) -> bool:
3        seen = set()
4        while(n>9):
5            if n not in seen:
6                seen.add(n)
7            else:
8                return False
9            n = sum(int(digit)**2 for digit in str(n))
10        return True if n==1 or n==7 else False
11