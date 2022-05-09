# Link: https://leetcode.com/problems/combinations/

n, k = map(int, input().split(" "))

ans = []
tmp = []
i = 1
size = 0

def Comb(n, k, i, size, tmp):

    if size == k:
        ans.append(tmp)
        tmp = []
    else:
        for j in range(i, n+1):
            Comb(n, k, j+1, size+1, tmp+[j])
    return ans

print(Comb(n, k, i, size, tmp))
