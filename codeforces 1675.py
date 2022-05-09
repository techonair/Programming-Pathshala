t = int(input())

def suspect(s):
    if len(s) == 1:
        return 1
    elif len(s) == 0:
        return 0
    else:
        n = len(s)
        for i in range(len(s)):
            if i > 0 and i < n - 1:
                print(s[i-1], s[i], s[i+1])
                if s[i-1] == "0" and s[i] == '0' and s[i+1] == '0':
                    cnt = n
                    return cnt
                elif s[i-1] == "?" and s[i] == '?' and s[i+1] == '?':
                    cnt = n
                    return cnt
                elif s[i-1] == "1" and s[i] == '1' and s[i+1] == '1':
                    continue
                elif s[i-1] == "1" and s[i] == '?' and s[i+1] == '0':
                    cnt = n - i - 1
                    return cnt
                elif s[i-1] == "0" and s[i] == '?' and s[i+1] == '1':
                    cnt = n-i-2
                    return cnt
                elif s[i-1] == "?" and s[i] == '0' and s[i+1] == '?':
                    cnt = n-i-1
                    return cnt
                elif s[i-1] == "?" and s[i] == '1' and s[i+1] == '?':
                    cnt = n-i-1
                    return cnt
                elif s[i-1] == "1" and s[i] == '1' and s[i+1] == '0':
                    cnt = 2
                    return cnt

for i in range(t):
    s = [i for i in input()]
    #a, b, c, x, y = map(int, input().split(" "))
    print("ans............ = ", suspect(s))