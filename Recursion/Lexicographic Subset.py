arr= [1,2,3]
ans = []
def subset(idx, tmp, l):
    
    if idx == len(arr):
        ans.append(tmp[:])
        return
    ans.append(tmp[:])
    for j in range(idx, len(arr)):
        subset(j+1, tmp + [arr[j]], l+1)
        
    
subset(0, [], 0)
print(ans)