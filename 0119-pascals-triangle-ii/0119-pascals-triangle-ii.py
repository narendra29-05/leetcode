class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rowIndex+=1
        answer=[[1]]
        for i in range(1,rowIndex):
            prev=answer[-1]
            row=[1]
            for j in range(1,i):
                row.append(prev[j-1]+prev[j])
            row.append(1)
            answer.append(row)
        return answer[-1]
        