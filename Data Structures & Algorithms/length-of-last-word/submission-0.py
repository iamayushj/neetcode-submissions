class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        lengthOfWord = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == ' ':
                return lengthOfWord
            else:
                lengthOfWord += 1
        return lengthOfWord