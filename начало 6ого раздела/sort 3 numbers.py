a = int(input())
b = int(input())
c = int(input())

s = a + b + c
M = max(a, b, c)
m = min(a, b, c)
print(M, s - M - m, m, sep='\n')
