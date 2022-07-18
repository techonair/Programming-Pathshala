t = int(input())

def func(arr):
    ans = 0
    for i in range(i==0, n-i-2):
        ans += arr[i] ^ arr[n-1-i]
        return (ans+1)/2

for i in range(t):
    n = int(input())
    #a, b = map(int, input().split(" "))
    arr = [int(i) for i in input().split(" ")]
    #b = [int(i) for i in input().split(" ")]
    #x, y = map(int, input().split())
    print("ans....", func(arr))
