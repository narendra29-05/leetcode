class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==0:
            return []
        answer=[[1]]
        for i in range(1,numRows):
            row=[1]
            prev=answer[-1]
            for j in range(1,i):
                row.append(prev[j-1]+prev[j])
            row.append(1)
            answer.append(row)
        return answer


