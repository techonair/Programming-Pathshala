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

for i in range(2, m):
    if spf[i] == -1:
        for j in range(i*i, m+1, i):
            if spf[j] == -1:
                spf[j] = i

print(spf[0:20])