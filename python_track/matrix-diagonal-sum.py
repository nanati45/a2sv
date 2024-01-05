class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        size=len(mat)
        primary=0
        i , j= 0, 0
        while i < size:
            primary+=mat[i][j]
            i+=1
            j+=1    

        secondary=0
        i , j = size - 1 , 0
        while i >= 0 :
            secondary+=mat[i][j]
            i-=1
            j+=1
        
        if len(mat[0]) % 2 ==0:     
            return primary + secondary 
        else :
            middle = size // 2
            return primary + secondary - mat[middle][middle]        