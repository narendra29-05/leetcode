class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low=0
        row=len(matrix)
        cols=len(matrix[0])

        high=row-1
        flag=0

        while low<=high:
            mid=(low+high)//2

            if target>=matrix[mid][0] and target <= matrix[mid][-1]:
                flag=1
                break
            if target > matrix[mid][-1]:
                low=mid+1
            else:
                high=mid-1
        if flag:
            low=0
            high=cols-1
            while low<=high:
                targetmid=(low+high)//2
                if matrix[mid][targetmid]==target:
                    return True
                if matrix[mid][targetmid]<target:
                    low=targetmid+1
                else:
                    high=targetmid-1
            return False
        return False
