class Solution:
    def longestPalindrome(self, s: str) -> str:
        window = len(s)
        flag = True
        while flag:
            for i in range(len(s)-window+1):
                a = s[i:i+window] 
                if a == a[::-1]:
                    # ans = a
                    flag = not flag
                    break
            window -= 1
        return a
