class Solution:
    def isPalindrome(self, s: str) -> bool:
        y = ''
        for x in s:
            if x.isalnum():
                y += x
        
        y = y.upper()
        if y == y[::-1]:
            return True
        return False
