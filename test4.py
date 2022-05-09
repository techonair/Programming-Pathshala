t = int(input())


def isPossible(x, y):
    flag = False
    if y % x == 0:
        d = y//x
        if d == 1:
            return 1, 1
        elif d < 1:
            return 0, 0
        for i in range(2, d+1):
            if d // (i*x) == 0:
                b = i
        #print("b ==", b)
        if b > 1:
            ans = x*b
            a = 1
            while (ans < y):
                ans = ans * b
                a += 1
            
        if ans == y:
            flag = True
        else:
            flag = False
    if flag:
        return a, b
    else:
        return 0, 0

for i in range(t):
    x, y = map(int, input().split(" "))
    result = isPossible(x, y)
    print(" ".join(str(i) for i in result))
