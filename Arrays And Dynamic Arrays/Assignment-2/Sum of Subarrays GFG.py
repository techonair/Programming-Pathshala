from ctypes.wintypes import LONG
from re import M


arr = [int(i) for i in input().split(',')]
n = len(arr)
m = 10**9 + 7
ans = 0
for i in range(n):
    contrib = (((( (i+1) % m) * ( (n-i) % m)) % m) * (arr[i] % m)) % m

    ans = ((ans % m) + (contrib % m)) % m

print(ans)
