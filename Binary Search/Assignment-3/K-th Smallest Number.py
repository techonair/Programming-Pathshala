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