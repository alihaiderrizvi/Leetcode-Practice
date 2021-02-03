class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        first = [1]
        second = [1,1]
        ans = [first, second]
        if numRows == 0:
            return []
        if numRows == 1:
            return [first]
        if numRows == 2:
            return [first, second]
        else:
            
            for x in range(numRows-2):
                lst = []
                for y in range(x+3):
                    if y == 0 or y == x+2:
                        lst.append(1)
                    else:
                        lst.append(ans[-1][y-1] + ans[-1][y])
                ans.append(lst)
        
        return ans
