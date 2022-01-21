matrix = [[1,4,7,11,15],
          [2,5,8,12,19],
          [3,6,9,16,22],
          [10,13,14,17,24],
          [18,21,23,26,30]]

target = 24

m = len(matrix)
n = len(matrix[0])

# starting position
i, j = 0, n-1
flag = False

# terminate while loop when in last row's first element or when key == target

while i < m and j >= 0:
        key = matrix[i][j]
        if key == target:
            flag = True
            break
        elif key > target:
            j = j-1
        elif key < target:
            i = i+1

if flag:
    print(True)
else:
    print(False)