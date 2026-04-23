class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
       if len(s1) > len(s2):
        return False 
       s1map = {}
       s2map = {}
       left = 0
       max_size = len(s1)
       for i in s1:
        s1map[i] = s1map.get(i, 0) + 1
       
       for right in range(len(s2)):
        s2map[s2[right]] = s2map.get(s2[right], 0) + 1

        if (right - left + 1) > max_size:
            s2map[s2[left]] -= 1
            if s2map[s2[left]] == 0:
                del s2map[s2[left]]
            left +=1

        if (right - left + 1) == max_size:
            if s2map == s1map:
                return True
       return False