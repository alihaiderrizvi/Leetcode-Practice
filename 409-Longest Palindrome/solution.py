class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = {}
        for i in s:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        ans = 0
        max_odd = 0
        for i in freq:
            if freq[i] % 2 == 0:
                ans += freq[i]
            else:
                if freq[i] > max_odd:
                    max_odd = freq[i]
                    letter = i
        for j in freq:
            if freq[j] % 2 == 1 and j != letter:
                ans += freq[j]-1
        ans += max_odd
        return ans
