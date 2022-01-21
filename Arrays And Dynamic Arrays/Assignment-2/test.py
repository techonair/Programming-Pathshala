#["Matrix", "sumRegion", "sumRegion", "sumRegion"]

matrix= [[3, 0, 1, 4, 2], 
         [5, 6, 3, 2, 1],
         [1, 2, 0, 1, 5],
         [4, 1, 0, 1, 7],
         [1, 0, 3, 0, 5]] 
'''
matrix = [[1, -3],
          [-4, 9]] '''

row1 = 1
col1 = 2
row2 = 2
col2 = 4

# Prefix Sum of Matrix

row = len(matrix)
col = len(matrix[0])

for i in range(row):
    for j in range(1, col):
        matrix[i][j] += matrix[i][j-1]

for i in range(1, row):
    for j in range(col):
        matrix[i][j] += matrix[i-1][j]

# Answer: (area0 - area1 - area2 + common_area)
# Edge cases exists: handled with if statements

area0 = matrix[row2][col2]

area1 = 0
if row1 - 1 >= 0:
    area1 = matrix[row1-1][col2]

area2 = 0
if col1 -1 >= 0:
    area2 = matrix[row2][col1-1]

common_area = 0
if area1 != 0 and area2 != 0:
    common_area = matrix[row1-1][col1-1]

ans = area0 - area1 - area2 + common_area

print(matrix)
print(area0, area1, area2, common_area)
print(ans)