class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''original_str = "".join(ch.lower() for ch in s if ch.isalnum())
        return(original_str == original_str[::-1])'''
        left = 0
        right = len(s) - 1

        while (left < right):
            if not s[left].isalnum():
                left = left + 1
            elif not s[right].isalnum():
                right = right - 1    
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left = left + 1
                right = right -1 
            
        return True