class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        j = 0
        flag = True
        for k in range(len(min(strs))):
            for i in range(len(strs)-1):
                if strs[i][j] != strs[i+1][j]:
                    flag = False
            if not flag:
                break
            j += 1
        if j == 0:
            return ""
        return strs[0][0:j]
