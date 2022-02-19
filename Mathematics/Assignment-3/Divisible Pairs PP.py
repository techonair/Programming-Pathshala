# Problem: https://dashboard.programmingpathshala.com/practice/question?questionId=45&sectionId=1&moduleId=1&topicId=2&subtopicId=30&assignmentId=6

n = int(input())
arr = [int(i) for i in input().split()]

k = 5
cnt = [0]*k
for i in range(n):
    cnt[arr[i]%k] += 1

ans = 0
ans+= cnt[0]*(cnt[0]-1)/2

for i in range(1,int(k/2)):
    ans+= cnt[i]*cnt[k-i]
    # edge case of even number
    if k%2 == 0:
        ans += cnt[k/2]*(cnt[k/2]-1)/2
    else:
        ans += cnt[int(k/2)]*cnt[int(k/2)+1]
    
print(int(ans))
