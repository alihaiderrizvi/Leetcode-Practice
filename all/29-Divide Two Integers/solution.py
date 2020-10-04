class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend > 0:
            div_sign = 0
        else:
            div_sign = 1
        if divisor > 0:
            dvs_sign = 0
        else:
            dvs_sign = 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        ans = dividend // divisor
        if (div_sign == 1 and dvs_sign == 1) or (div_sign == 0 and dvs_sign == 0):
            if ans > 2**31 -1:
                ans = 2**31 -1
            return ans
        else:
            if ans < -2**31:
                ans = -2**31
            return -ans
