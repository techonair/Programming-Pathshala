# Link: https://leetcode.com/problems/powx-n/

x = float(input())
n = float(input())

def myPow(x, n):
    # termination condition + edge case
    if (n == 0):
        return 1
    if abs(x) < 1e-40:
        return 0
    ans = myPow(x, int(n/2))
    if (n%2 == 0):
        return ans*ans
    # edge case if power is odd and -ve
    else:
        if(n > 0):
            return x * ans * ans
        else:
            return (ans * ans) / x


print(myPow(x, n))

#Test Cases
"""
2.00000
10
2.10000
3
2.00000
-2
34.00515
-3
8.84372
-5
"""
