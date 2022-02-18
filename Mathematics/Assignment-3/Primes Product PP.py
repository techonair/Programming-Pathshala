# Problem: https://dashboard.programmingpathshala.com/practice/question?questionId=44&sectionId=1&moduleId=1&topicId=2&subtopicId=30&assignmentId=6

from math import ceil
from math import sqrt

cnt = 1
n = int(input())
s = []
q = []
for i in range(n):
    l, r = map(int, input().split())
    s.append(l)
    q.append(r)

def Primes(L, R):
    
    # Preprocessing
    isPrimes = [1]*(int(sqrt(R))+1)
    isPrimes[0] = 0
    isPrimes[1] = 0

    for i in range(2, len(isPrimes)):
        if isPrimes[i] == 1:
            for j in range(i*i, len(isPrimes), i):
                isPrimes[j] = 0

    primes = []
    for i in range(2,len(isPrimes)):
        if isPrimes[i]:
            primes.append(i)
    # Till this step we have all the primes between 2 and R**(1/2)

    isPrimeLR = [1]*(R-L+1)

    for i in range(len(primes)):
        k = ceil(L*1.0/primes[i])
        for j in range(primes[i]*max(k,2), R+1, primes[i]):
            isPrimeLR[j-L] = 0
    return isPrimeLR

for i in range(n):
    prime_num = Primes(s[i], q[i])
    for num in range(1,len(prime_num)):
        if prime_num[num] == 1:
            cnt = (num%(10**9 +1) * cnt%(10**9 +1))%(10**9 +1)
            print(cnt)
    print(prime_num)
