class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        if len(mat)==1:
            return mat[0][0]
        p_d=s_d=0
        for i in range(len(mat[0])):
            p_d+=mat[i][i]
            s_d+=mat[i][-(i+1)]
        if len(mat)%2==1:
            p_d-=(mat[len(mat)//2][len(mat)//2])
        return p_d+s_d