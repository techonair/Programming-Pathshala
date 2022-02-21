# Problem: https://dashboard.programmingpathshala.com/practice/question?questionId=53&sectionId=1&moduleId=1&topicId=2&subtopicId=36&assignmentId=7

n = int(input())

def brackets(N):
    
    catalan = [0]*(N+1)
    catalan[0] = 1
    catalan[1] = 1
    m = (10**9)+7

    for i in range(2,N+1):
        for j in range(i):
            catalan[i] = (catalan[i] % m) + ((catalan[j] % m) * (catalan[i-j-1] % m)) % m
    return catalan[N]

if n % 2 != 0:
    ans = -1
else:
    ans = brackets(n//2)

print(ans)