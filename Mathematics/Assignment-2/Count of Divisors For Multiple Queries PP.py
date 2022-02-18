# Problem: https://dashboard.programmingpathshala.com/practice/question?questionId=32&sectionId=1&moduleId=1&topicId=2&subtopicId=25&assignmentId=5

t = int(input())
n = []
q = []

for i in range(t):
    tm = int(input())
    n.append(tm)
    tp = [int(i) for i in input().split()]
    q.append(tp)

m = 10**6
spf = [-1]*(m+1)

for i in range(2, m+1):
    if spf[i] == -1:
        for j in range(i**2, m+1, i):
            if spf[j] == -1:
                spf[j] = i

for i in range(t):
    for j in range(n[i]):
        cnt = []
        num = q[i][j]
        cnt.append(1)
        p = 0
        while spf[num] != -1:
            cnt[p] += 1
            num = int(num/spf[num])
        if num != 1:
            if spf[num] != -1:
                cnt.append(1)
        power = 1
        for k in cnt:
            power += power * (k+1)
        print(power-1, end= " ")