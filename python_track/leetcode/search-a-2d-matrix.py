class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col = len(matrix[0])
        row = len(matrix)
        left = 0 
        right = row * col - 1
        while left <= right :
            mid = left + (right - left) // 2
            num = matrix[mid // col][mid % col]
            if num > target :
                right = mid - 1
            elif num < target :
                left = mid + 1
            else:
                return True
        return False                
