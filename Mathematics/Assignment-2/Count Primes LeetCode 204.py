# Problem: https://leetcode.com/problems/count-primes/

# Method1: 
# Time Complexity: O( N*sqrt(N) ), Space Complexity: O(1)
"""
from cmath import sqrt

n = int(input())

ans = 0
for i in range(2, n):
    cnt = 0
    tmp = sqrt(i)
    for j in range(2, int(tmp.real)+1):
        if i%j==0:
            cnt += 1
            break
    if cnt == 0:
        ans += 1

print(ans)
"""

# Method 2: 
# Time Complexity: O(N*log(logN)), Space Complexity: O(N)

n = int(input())
isPrime = [True]*n
isPrime[1] = False

cnt = 0
for i in range(2,n):
    if isPrime[i] == True:
        cnt += 1
        for j in range(i*i,n,i):
            isPrime[j] = False

print(cnt)

# Same as Method 2 just a little faster but memory consumption is almost O(2N)
"""
n = int(input())
isPrime = [True]*n
isPrime[1] = False

cnt = 0
for i in range(2,n):
    if isPrime[i] == True:
        cnt += 1
        # below implementation is faster than 'for loop'
        if i*i <n:
            l = len(isPrime[i*i::i])
            isPrime[i*i::i]= [False]*l

print(cnt)
"""