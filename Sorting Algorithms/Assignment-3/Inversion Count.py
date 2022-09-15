# link: https://practice.geeksforgeeks.org/problems/inversion-of-array-1587115620/1


# Method 1: Brute Force (TLE: 100/117)
def inversionCount(self, arr, n):
    
    cnt = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                cnt += 1
    return cnt

"""
Time Complexity = O(N^2)

Space Complexity = O(1)
"""

# Method 2: Inversion Count and Inter Array Inversion Count

