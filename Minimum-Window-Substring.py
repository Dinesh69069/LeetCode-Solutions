class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_map = {}
        window_map = {}
        have , need = 0 , 0
        for i in t :
            if i in target_map:
                target_map[i] +=1
            else:
                target_map[i] = 1
                need+=1
        left , min_len ,min_str = 0 , len(s)+1 , ''
        for right in range(len(s)):
            if s[right] in window_map:
                window_map[s[right]] +=1
            else:
                window_map[s[right]] = 1
            if((s[right] in target_map) and (window_map[s[right]] == target_map[s[right]])):
                have +=1
            while(need==have):
                if((right - left + 1) < min_len ):
                    min_len = right - left +1
                    min_str = s[left:right+1]
                window_map[s[left]] -=1
                if((s[left] in target_map) and (window_map[s[left]]<target_map[s[left]])):
                    have-=1
                left+=1
        return min_str


