# Problem: https://dashboard.programmingpathshala.com/practice/question?questionId=27&sectionId=1&moduleId=1&topicId=2&subtopicId=19&assignmentId=4

"""
You are given two numbers A and B. Print two integers X and Y where 
X = GCD(A,B) and Y = LCM(A,B).
"""
# METHOD 1:
a, b = map(int, input().split())

n = min(a, b)
if n == 0:
    gcd = max(a, b)
else:
    for i in range(1, n+1):
        if a % i == 0 and b % i == 0:
            gcd = i

lcm = int(a*b/gcd)

print(gcd, lcm)

# Time Complexity: O(min(A,B))

# METHOD 2: Euclid's GCD Algorithm

#a, b = map(int, input().split())
max_n = max(a, b)
min_n = min(a,b)

while (max_n % min_n != 0):
    tmp = max_n % min_n
    max_n = min_n
    min_n = tmp

lcm2 = int(a*b/min_n)
print(min_n, lcm2)

# Time Complexity: O( log(max(A,B)) )


