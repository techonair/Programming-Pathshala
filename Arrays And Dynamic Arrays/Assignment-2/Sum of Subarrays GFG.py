# Problem : https://practice.geeksforgeeks.org/problems/sum-of-subarrays2229/1#

a = [int(i) for i in input().split(',')]
n = len(a)

m = 10**9 + 7
ans = 0
for i in range(n):
    contrib = (((( (i+1) % m) * ( (n-i) % m)) % m) * (a[i] % m)) % m

    ans = ((ans % m) + (contrib % m)) % m

print(ans)
