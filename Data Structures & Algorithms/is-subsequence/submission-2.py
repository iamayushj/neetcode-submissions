class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if ( len(s) > len(t)):
            return False
        sPointer = 0
        tPointer = 0

        while (tPointer < len(t)):
            if (s[sPointer] == t[tPointer]):
                sPointer += 1
                tPointer += 1
                if sPointer == len(s):
                    return True
            else:
                tPointer += 1
        return False

