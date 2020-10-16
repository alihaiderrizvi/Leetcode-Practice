class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, new_color: int) -> List[List[int]]:
        old_color = image[sr][sc]
        if old_color == new_color:
            return image
        queue = [[sr,sc]]
        
        while queue:
            sr,sc = queue.pop(0)
            image[sr][sc] = new_color
            
            if sr > 0 and image[sr-1][sc] == old_color:
                queue.append([sr-1, sc])
            if sc > 0 and image[sr][sc-1] == old_color:
                queue.append([sr, sc-1])
            if sr < len(image)-1 and image[sr+1][sc] == old_color:
                queue.append([sr+1, sc])
            if sc < len(image[0])-1 and image[sr][sc+1] == old_color:
                queue.append([sr, sc+1])
        
        return image
