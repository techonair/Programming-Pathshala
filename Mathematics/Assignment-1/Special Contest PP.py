# Problem: https://dashboard.programmingpathshala.com/practice/question?questionId=29&sectionId=1&moduleId=1&topicId=2&subtopicId=19&assignmentId=4

q = int(input())
ans = []
for i in range(q):
    n, a, b, k = map(int, input().split())
    min_m = min(a,b)
    max_m = max(a,b)
    if min_m > 0:
        while (max_m % min_m != 0):
            tmp = max_m % min_m
            max_m = min_m
            min_m = tmp
        gcd = min_m
    else:
        gcd = max_m

    lcm = (a*b)//gcd
    # only divisible by a or b, not a and b 
    cnt = n//a + n//b - 2*(n//lcm)
    if cnt >= k:
        ans.append('Win')
    else:
        ans.append('Lose')

for i in ans:
    print(i)
