# Problem: https://dashboard.programmingpathshala.com/practice/question?questionId=46&sectionId=1&moduleId=1&topicId=2&subtopicId=36&assignmentId=7

n, m, x = map(int, input().split())

# use of pascal triangle to get value of (n+m)C(x)
pascal = [[0 for j in range(61)] for i in range(61)]

pascal[0][0] = 1

for i in range(1,61):
    for j in range(0,i+1):
        if j == 0 or j == i:
            pascal[i][j]= 1
        else:
            pascal[i][j] = pascal[i-1][j-1]+pascal[i-1][j]

ans = 0
ans += pascal[n+m][x]

# edge case 1: x<=m
if x <= m:
    ans -= pascal[m][x]

# edge case 2: x-1<=m
if x-1<=m:
    ans -= n * pascal[m][x-1]

# edge case 3: x-2<=m
if x-2<=m:
    ans-= (n*(n-1)//2)*(pascal[m][x-2])

# edge case 4: x-3<=m
if x-3<=m:
    ans-= (n*(n-1)*(n-2)//6)*(pascal[m][x-3])

# # edge case 5: x<=n
if x<=n:
    ans-= pascal[m][0]

print(ans)