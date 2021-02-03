class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        B = []
        C = []
        for x in A:
            if x % 2 == 0:
                B.append(x)
            else:
                C.append(x)
        final = B+C
        return final
