t = int(input())

def xorgand(arr, l, r, x):
    cnt = 0
    for i in range(l-1, r):
        if arr[i] ^ x > arr[i] & x:
            cnt += 1
            print("xor : ", arr[i] ^ x)
            print("& : ",  arr[i] & x)
    return cnt
    

for i in range(t):
    n = int(input())
    #arr = map(int, input().split())
    arr = [int(i) for i in input().split()]
    q = int(input())
    for _ in range(q):
        l, r, x = map(int, input().split())
        print("ans", xorgand(arr, l, r, x))
