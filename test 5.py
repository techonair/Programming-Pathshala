t = int(input())

def last(n, l):
    one = 0
    zero = 0
    for i in l:
        if i == 1:
            one += 1
        else:
            zero += 1

    while one + zero > 1:
        # Alice : OR
        if one > 0:
            if zero > 0:
                zero -= 1
            else:
                one -= 1
        else:
            zero -= 1
        if one + zero > 1:
            pass
        else:
            break
        # Bob : AND
        if one > 0:
            if zero > 0:
                one -= 1
        elif zero > 0:
            zero -= 1
    if one == 1:
        return 1
    else:
        return 0

for i in range(t):
    n = int(input())
    l = [int(i) for i in input().split(" ")]
    print(last(n, l))


