class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        mt=[]
        for i in range(len(matrix[0])):
            col=[]
            for j in range(len(matrix)):
                col.append(matrix[j][i])
            mt.append(col)
        return mt        