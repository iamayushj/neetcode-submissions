class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        '''s = s.strip()
        lengthOfWord = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == ' ':
                return lengthOfWord
            else:
                lengthOfWord += 1
        return lengthOfWord'''
        i = len(s) - 1
        lengthOfWord = 0
        while s[i] == ' ':
            i -= 1
        while s[i] != ' ' and i >= 0:
            lengthOfWord += 1
            i -= 1
        return lengthOfWord
