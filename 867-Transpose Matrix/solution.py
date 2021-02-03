class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        l = []
        for x in range(len(A[0])):
            a = []
            for y in A:
                a.append(y[x])
            l.append(a)
            
        return l
