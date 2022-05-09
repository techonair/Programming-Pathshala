t = int(input())

def password(n, arr, special):
    for i in range(n):
        if arr[i] in special:
            arr[i] = 1
            idx = i+1
        else:
            arr[i] = 0
    cnt = 0
    tmp = 0
    c = 1
    for i in range(idx):
        if arr[i] == 0:
            tmp +=1
            if tmp > cnt:
                cnt = max(cnt, tmp)
                tmp = cnt-tmp
        elif arr[i] == 1:
            if c != 1: 
                cnt += 1
            c += 1
    return n, arr, special, cnt
    

for i in range(t):
    n = int(input())
    arr = [i for i in input()]
    special= list(input().split(" "))[1:]
    print(password(n, arr, special))
