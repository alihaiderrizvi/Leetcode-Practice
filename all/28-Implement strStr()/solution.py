class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        len_needle = len(needle)
        if needle == haystack:
            return 0
        for x in range(len(haystack)):
            if haystack[x:x+len_needle] == needle:
                return x
