class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stk = []
        for i in s:
            if i == "(" or i == "[" or i == "{":
                stk.append(i)
            elif stk and ((i == ")" and stk[-1] == "(") or (i == "]" and stk[-1] == "[") or (i == "}" and stk[-1] == "{")):
                stk.pop()
            else:
                return False
        return not stk
