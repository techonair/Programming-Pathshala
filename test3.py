cards = [i for i in input().split(',')]

dic =  {}
for i in range(len(cards)):
    array = []
    for j in range(len(cards)):
        if cards[i] == cards[j]:
            array.append(j)
    dic[cards[i]] = array

ans = []
for key, value in dic.items():
    if len(value) > 1:
        print('k', key)
        m = 1+ 10**6
        for i in range(len(value)):
            if i < len(value)-1:
                print(m)
                m = min(m, value[i+1] - value[i]+1)
                print(m)
                ans.append(m)
print(dic)
print(ans)
if len(ans) > 0:
    print(min(ans))
else:
    print(-1)

            



