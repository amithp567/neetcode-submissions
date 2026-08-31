class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        rows = len(self.matrix)
        cols = len(self.matrix[0])
        sum = 0
        for i in range(rows):
            for j in range(cols):
                if i>= row1 and i<=row2 and j>=col1 and j<=col2:
                    sum += self.matrix[i][j]
        return sum
        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)