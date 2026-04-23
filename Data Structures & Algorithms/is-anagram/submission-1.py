class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
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
        return (sorted(list(s)) == sorted(list(t)))