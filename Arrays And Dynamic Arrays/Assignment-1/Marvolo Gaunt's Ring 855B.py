# Problem : https://codeforces.com/problemset/problem/855/B

n, p, q, r = map(int, input().split())

arr = [int(i) for i in input().split()]

Pmax = [-10**9] * n
Pmax[0] = p * arr[0]

for i in range(1, n):
    Pmax[i] = max(Pmax[i-1], p * arr[i])

Smax = [-10**9] * n
Smax[n-1] = r * arr[n-1]

for i in range(n-2, -1, -1):
    Smax[i] = max(Smax[i+1], r * arr[i])

ans = Pmax[0] + q * arr[0] + Smax[0]

for i in range(1, n):
    ans = max(ans, Pmax[i] + q * arr[i] + Smax[i])

print(ans)

