class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        shortestLenWord = min(len(word) for word in strs) 
        for i in range(shortestLenWord):
            char_to_be_matched = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != char_to_be_matched:
                    return prefix
            prefix += char_to_be_matched
        return prefix