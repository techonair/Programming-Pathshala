# link: https://www.spoj.com/problems/AGGRCOW/

t = int(input())
n, c = map(int, input().split())

def LargestCowtoCowDistance(stall, n, cows):
	
	low = stall[0]
	high = stall[n-1]-stall[0]
	
	while low<=high:
		m = (low+high)//2
		
		if not allCowsPlaced(m, cows):
			high = m-1
		else:
			if not allCowsPlaced(m+1, cows):
				return m
			low = m+1

def allCowsPlaced(m, cows):
	
	total_cows_placed = 1
	last_cow_located = stall[0]
	
	for i in range(1,n):
		
		if stall[i]-last_cow_located < m:
			continue
		else:
			total_cows_placed += 1
			last_cow_located = stall[i]
			if total_cows_placed == cows:
				break
	
	return total_cows_placed == cows
	

for _ in range(t):
	
	stall = []
	for i in range(n):
		stall.append(int(input()))
	stall.sort()
	print('ans', LargestCowtoCowDistance(stall, n, c))
	
"""
Time Complexity: O( Q(Nlogn + log(max-min)) )
Space Complexity: O(N)
"""