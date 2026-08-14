class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        sPointer = 0
        tPointer = 0
        while tPointer < len(t) and sPointer < len(s):
            if s[sPointer] == t[tPointer]:
                sPointer += 1
                tPointer += 1
            else:
                sPointer += 1
        return len(t) - tPointer