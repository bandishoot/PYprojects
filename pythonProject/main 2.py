N = str(input())
x = len(N)
for i in range(x-1):
    a = 1
    while N[i] == N[i+1]:
        a += 1
    print(N[i] + str(a), end="")
print(N[-1] + str(a))
