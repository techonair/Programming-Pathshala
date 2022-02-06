# Problem: https://www.geeksforgeeks.org/sum-of-all-submatrices-of-a-given-matrix/

arr = [[ 1, 1, 1 ], [ 1, 1, 1 ], [ 1, 1, 1 ]]

n = len(arr)

ans = 0

for i in range(n):
    for j in range(n):
        top = (i+1) * (j+1)
        bottom = (n-i) * (n-j)
        ans += top * bottom * arr[i][j]

print(ans)