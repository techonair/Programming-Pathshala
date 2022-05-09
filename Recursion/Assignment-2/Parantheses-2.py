# Link: https://www.hackerrank.com/contests/gl-bajaj-self-evaluation-evening-batch/challenges/bracket-challenge-1/problem

n = int(input())

l = 0
r = 0
x = 0
y = 0
i = 0
s = ""
ans = []
stk = []

def PP(l, r, x, y, i, s, stk):
    if i == 4*n:
        ans.append(s)
        return
    if len(stk) == 0:
        stk.append("(")
        PP(l+1, r, x, y, i+1, s+"(", stk)
        stk.append("{")
        PP(l, r, x, y, i+1, s+"{", stk)
    else:
        if stk[len(stk)-1] == "(":
            if l < n:
                PP(l+1, r, x, y, i+1, s+"(", stk)
                if len(stk) != 0:
                    stk.pop()
            else:
                PP(l, r+1, x, y, i+1, s+")", stk)
                if len(stk) != 0:
                    stk.pop()
            if x < n:
                PP(l, r, x+1, y, i+1, s+"{", stk)
                if len(stk) != 0:
                    stk.pop()
            else:
                PP(l, r, x, y+1, i+1, s+"}", stk)
                if len(stk) != 0:
                    stk.pop()
            
    
PP(l, r, x, y, i, s, stk)
print(ans)

