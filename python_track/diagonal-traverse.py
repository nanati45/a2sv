class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagonals=defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i+j in diagonals:
                    diagonals[i+j].append(mat[i][j])
                else:
                   diagonals[i+j]=[mat[i][j]]  
        ans=[]
        for i in diagonals : 
            if i%2==0:
                diagonals[i]=diagonals[i][::-1]
            ans.extend(diagonals[i])
              
        return ans          
