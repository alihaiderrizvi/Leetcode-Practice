class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        lst = []
        for z in matrix:
            lst.append([])
        for i in range(len(matrix)-1,-1,-1):
            
            for j in range(len(matrix)):
                
                lst[j].append(matrix[i][j])
        for u in range(len(lst)):
            for v in range(len(lst)):
                matrix[u][v] = lst[u][v]
