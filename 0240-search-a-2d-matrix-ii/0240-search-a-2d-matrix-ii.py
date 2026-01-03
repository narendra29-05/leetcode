class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        l=0
        rows=len(matrix)   #5
        cols=len(matrix[0]) #5
        r=cols-1
        while l<rows and r>=0:
            if matrix[l][r]==target:
                return True
            if matrix[l][r]>target:
                r-=1
            else:
                l+=1
        return False
