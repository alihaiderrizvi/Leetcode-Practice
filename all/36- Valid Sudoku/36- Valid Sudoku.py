class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            s = set()
            for j in i:
                if j != '.':
                    if j in s:
                        return False
                    else:
                        s.add(j)
        
        for i in range(len(board)):
            s = set()
            for j in range(len(board)):
                if board[j][i] != '.':
                    if board[j][i] in s:
                        return False
                    else:
                        s.add(board[j][i])
        
        lists = []
        
        for i in range(0,9,3):
            for j in range(0,9,3):
                lst = []
                for k in range(3):
                    for l in range(3):
                        if board[i+k][j+l] != '.':
                            lst.append(board[i+k][j+l])
                lists.append(lst)
        
        for l in lists:
            if len(l) != len(set(l)):
                return False
        return True
