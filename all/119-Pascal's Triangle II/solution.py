class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        first = [1]
        second = [1,1]
        ans = [first, second]
        if rowIndex == 0:
            return first
        if rowIndex == 1:
            return second
        else:
            
            for x in range(rowIndex-1):
                lst = []
                for y in range(x+3):
                    if y == 0 or y == x+2:
                        lst.append(1)
                    else:
                        lst.append(ans[-1][y-1] + ans[-1][y])
                ans.append(lst)
        
        return ans[-1]
