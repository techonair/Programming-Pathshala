# Problem: https://dashboard.programmingpathshala.com/practice/question?questionId=31&sectionId=1&moduleId=1&topicId=2&subtopicId=25&assignmentId=5

t = int(input())
q = []
for i in range(t):
    q.append(int(input()))

n = max(q)
isPrime = [1]*(n+1)
spf = [-1]*(n+1) #Smallest Prime Factor
isPrime[1] = 0

for i in range(2, n+1):
    if isPrime[i] == 1:
        for j in range(i*i,n+1,i):
            # storing the lowest prime that divides num n in power array
            isPrime[j] = 0
            if spf[j] == -1:
                spf[j] = i
print(isPrime[0:21])
print(spf[0:21])
# below code is not working
for num in q:
    power = 0
    while spf[num] != -1:
        power += 1
        num = int(num/spf[num])
        if spf[num] == -1:
            print(spf[num-1], power)
    if num != 1:
        print(num, 1)