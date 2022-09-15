def count(i):
    c = 0
    for num in nums:
        if num < nums[i]:
            c += 1
    return c

low = min(nums)
high = max(nums)

while low <= high:
    m = (low+high)//2
    cnt = count(m)
    
    if cnt < k:
        low = m+1
    else:
        if cnt < k:
            return m
        high = m-1

# Time Complexity: O(Nlog(max-min))
#######################################
# Same logic:

arr = [int(i) for i in input().split(', ')]
k = int(input())

def count(num):
    cnt = 0
    for i in range(len(arr)):
        if arr[i] <= num:
            cnt += 1
    return cnt

low = min(arr)
high = max(arr)

while low <= high:
    mid = (low+high)//2

    if count(mid) < k:
        low = mid+1
    elif count(mid) >= k:
        if count(mid-1) < k:
             print(mid)
        high = mid-1