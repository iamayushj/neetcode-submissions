class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        left = 0
        window_map = {}
        t_map = {}
        formed = 0

        for ch in t:
            t_map[ch] = t_map.get(ch, 0) + 1

        required = len(t_map)

        min_len = float("inf")
        start = 0

        for right in range(len(s)):
            window_map[s[right]] = window_map.get(s[right], 0) + 1

            if s[right] in t_map and window_map[s[right]] == t_map[s[right]]:
                formed += 1

            while formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left

                window_map[s[left]] -= 1

                if s[left] in t_map and window_map[s[left]] < t_map[s[left]]:
                    formed -= 1

                left += 1

        return "" if min_len == float("inf") else s[start:start + min_len]