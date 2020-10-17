class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i in range(len(A)):
            copy_lst = []
            for j in range(len(A[i])):
                copy_lst = [A[i][j]] + copy_lst
                
            A[i] = copy_lst
            
        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j] == 1:
                    A[i][j] = 0
                else:
                    A[i][j] = 1
        
        return A
