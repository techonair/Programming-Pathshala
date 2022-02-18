# Problem: https://dashboard.programmingpathshala.com/practice/question?questionId=31&sectionId=1&moduleId=1&topicId=2&subtopicId=25&assignmentId=5

t = int(input())
q = []
for i in range(t):
    q.append(int(input()))

n = 10**6
spf = [-1]*(n+1) # Smallest Prime Factor

for i in range(2,n+1):
    if spf[i] == -1:
        for j in range(i**2, n+1, i):
            # storing the lowest prime that divides num n in power array
            if spf[j] == -1:
                spf[j] = i

# little bit of problem here
print(spf[0:26])
for i in range(t):
    num = q[i]
    power = 0
    print(spf[num], end=' ')
    while spf[num] != -1:
        num = int(num/spf[num])
        power += 1
    print(power)
    if num != 1:
        print(num, 1)
