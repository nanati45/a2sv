class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        print(matrix)
        for i in range(1,len(matrix)):
            for j in range(i,-1,-1):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        return matrix         