# Link: https://leetcode.com/problems/permutation-sequence/



# Programming Pathshala Logic: But because we are generating all the permutaion that's why it a O(n!*n) which will give us TLE in above LeetCode problem
"""
def rightRotate(i, j, aux):
    tmp = aux[j]
    for x in range(j-1, i-1, -1):
        aux[x+1] = aux[x]
    aux[i] = tmp

def leftRotation(i, j, aux):
    tmp = aux[i]
    for i in range(i+1, j+1):
        aux[i-1] = aux[i]
    aux[j] = tmp

def permutation(n, k, i, aux):
    if i == n:
        #print(aux)
        ans.append(aux.copy())
        return
    for j in range(i, n):
        rightRotate(i, j, aux)
        permutation(n, k, i+1, aux)
        leftRotation(i, j, aux)

ans= []
n, k = map(int, input().split(" "))
arr = [i for i in range(1, n+1)]
permutation(n, k, 0, arr)
print("".join(str(i) for i in ans[k-1]))"""