class NumMatrix:

    def __init__(self, matrix):
        self.matrix = matrix
        row = len(matrix)
        col = len(matrix[0])

        for i in range(row):
            for j in range(1, col):
                self.matrix[i][j] += matrix[i][j-1]

        for i in range(1, row):
            for j in range(col):
                self.matrix[i][j] += self.matrix[i-1][j]

    def sumRegion(self, row1, col1, row2, col2):
        area0 = self.matrix[row2][col2]

        area1 = 0
        if row1 - 1 >= 0:
            area1 = self.matrix[row1-1][col2]

        area2 = 0
        if col1 -1 >= 0:
            area2 = self.matrix[row2][col1-1]

        common_area = 0
        if area1 != 0 and area2 != 0:
            common_area = self.matrix[row1-1][col1-1]

        ans = area0 - area1 - area2 + common_area
        
        return ans

