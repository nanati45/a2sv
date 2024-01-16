class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.rows=(len(matrix))
        self.cols=len(matrix[0])
        self.new_=[[0]*(self.cols+1) for r in range(self.rows+1)]
        for r in range(self.rows):
            prefix=0
            for c in range(self.cols):
                prefix+=matrix[r][c]
                above = self.new_[r][c+1]
                self.new_[r+1][c+1]=prefix + above
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        bottomRight=self.new_[row2+1][col2+1]
        above=self.new_[row1][col2+1]
        left=self.new_[row2+1][col1]
        topLeft=self.new_[row1][col1]
        ans=bottomRight-above-left+topLeft
        return (ans)


        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)