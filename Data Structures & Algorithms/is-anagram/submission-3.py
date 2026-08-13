class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hm_s = {}
        hm_t = {}
        
        for i in range(len(s)):
            hm_s[s[i]] = hm_s.get(s[i], 0) + 1
            hm_t[t[i]] = hm_t.get(t[i], 0) + 1
        
        return hm_s == hm_t

        '''
        if len(s) != len(t):
            return False
        s_map = {}
        t_map = {}

        for x in s:
            s_map[x] = s_map.get(x,0) + 1

        for y in t:
            t_map[y] = t_map.get(y,0) + 1
        
        return s_map == t_map
        '''
        '''return (sorted(list(s)) == sorted(list(t)))'''