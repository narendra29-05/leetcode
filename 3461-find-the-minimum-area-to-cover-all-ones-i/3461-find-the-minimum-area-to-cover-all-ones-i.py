

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        top,cols=len(grid),len(grid[0]) #---->top==len(grid)-->2,bottome=3--grid[0]--.3

        rows=top

        bottom=-1
        left=cols
        right=-1

        for i in range (rows):
            for j in range (cols):
                if grid[i][j]==1:
                    top=min(top,i)
                    bottom=max(bottom,i)
                    left=min(left,j)
                    right=max(right,j)
        if bottom==-1:
            return 0
        return (bottom-top+1)*(right-left+1)
