class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        prevColor = image[sr][sc]
        if image[sr][sc] == color:
            return image
        
        def dfs(x,y):
            if x< 0 or x >= len(image) or y< 0 or y >= len(image[0]) or  image[x][y] != prevColor:
                return
        
            image[x][y] = color
            
            dfs(x+1,y)
            dfs(x-1,y)
            dfs(x,y-1)
            dfs(x,y+1)
        
        dfs(sr,sc)
        
        return image

        