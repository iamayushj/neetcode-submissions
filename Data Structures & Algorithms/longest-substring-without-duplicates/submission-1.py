class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #s="xyzzxyz"
        res_set=set()
        left  = 0
        max_length = 0
        #xyzzxyz
        for right in range(len(s)):
          #print("res_set after loop ", res_set)
          while s[right] in res_set:
            res_set.remove(s[left])
            left += 1
            #print("res_set after remove ", res_set)
          res_set.add(s[right])
          #print("res_set after add ", res_set)
          max_length = max(max_length, right - left + 1)
        #print(res_set)
        return max_length