class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt_map = {}
        left = 0
        max_cnt = 0
        window_size = 0
        max_length = 0
        for right in range(len(s)):
          cnt_map[s[right]] = cnt_map.get(s[right], 0) + 1

          max_cnt = max(max_cnt, cnt_map[s[right]])
          if ((right - left + 1) - max_cnt) > k:
            cnt_map[s[left]] -= 1
            left += 1

          max_length = max(max_length, right - left + 1)
        return max_length
