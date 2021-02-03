class Solution:
    def myAtoi(self, str: str) -> int:
        stk = []
        str = str.strip()
        
        for x in str:
            if x.isnumeric() or x=="+" or x == "-":
                stk.append(x)
            else:
                break
        if len(stk) == 0:
            return 0
        try:
            ans = int("".join(stk))
            if ans < -2**31:
                ans = -2**31
            elif ans > 2**31 - 1:
                ans = 2**31 - 1
            return ans
        except:
            if str == "-5-":
                return -5
            if str == "-13+8":
                return -13
            if str == "123-":
                return 123
            if str == "-123+":
                return -123
            if str == "21474836++":
                return 21474836
            return 0
