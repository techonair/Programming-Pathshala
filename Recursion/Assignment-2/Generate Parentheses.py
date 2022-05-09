# Link: https://leetcode.com/problems/generate-parentheses/

n = int(input())

l = 1
r = 0
i = 1
s = "("
ans = []
def PP(l, r, i, s):
    if i == 2*n:
        ans.append(s)
        return
    if (l == r):
        s = s + "("
        PP(l+1, r, i+1, s)
    elif r < l:
        if l == n:
            PP(l, r+1, i+1, s+')')
        else:
            PP(l+1, r, i+1, s+'(')
            PP(l, r+1, i+1, s+')')
            

PP(l, r, i, s)
print(ans)