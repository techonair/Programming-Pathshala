# Problem: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

digit = str(input())

digitMap = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'],
['m','n','o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]

ans = [None]*(len(digit)+1)
i = 0
def letterComb(tmp, i, digit, digitMap):
    if len(digit) == 0:
        print(tmp)
        return

    for j in range( len(digitMap[ord(digit[i])-ord('2')])+1 ):
        tmp[i] = str(digitMap[ord(digit[i])-ord('2')][j])
        letterComb(tmp, i+1, digit, digitMap)

    print(ans)
letterComb(tmp, i, digit)