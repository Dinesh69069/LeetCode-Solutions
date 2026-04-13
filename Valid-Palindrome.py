1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        res = []
4        for i in range(len(s)):
5            if(s[i].isalnum()):
6                res.append(s[i])
7        rs = ''.join(res).lower()
8        return rs == rs[::-1]
9        