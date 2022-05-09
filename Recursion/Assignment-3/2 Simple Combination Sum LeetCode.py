# Link: https://leetcode.com/problems/combination-sum-iii/

k, n = map(int, input().split(" "))

ans = []
tmp = []
size = 0
sum = 0
i = 1

def isCombSum(n, k, i , size, sum, tmp):
    if size == k and sum == n:
        ans.append(tmp)
    if i < 10 and size < k and sum < n:
        isCombSum(n, k, i+1, size, sum, tmp)
        isCombSum(n, k, i+1, size+1, sum+i, tmp+[i])
    return ans

print(isCombSum(n, k, i, size, sum, tmp))