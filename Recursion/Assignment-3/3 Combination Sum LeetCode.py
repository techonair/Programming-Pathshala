# Link : https://leetcode.com/problems/combination-sum/

candidates = [int(i) for i in input().split(",")]
target = int(input())
ans = []
tmp = []
sum = 0
i = 0
def Comb(i, sum, tmp):
    if sum == target:
        ans.append(tmp)
        tmp = []
    elif i >= len(candidates) and sum > target:
        return
    elif i < len(candidates) and sum < target:
        Comb(i, sum+candidates[i], tmp+[candidates[i]])
        Comb(i+1, sum, tmp)
    return ans

print(Comb(i, sum, tmp))