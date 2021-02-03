class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        lst = []
        for x in range(left, right+1):
            cnt = 0
            for y in str(x):
                if y == '0' or x % int(y) != 0:
                    break
                elif x % int(y) == 0:
                    cnt += 1
            if cnt == len(str(x)):
                lst.append(x)
        
        return lst
