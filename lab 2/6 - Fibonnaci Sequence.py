N = int(input())
fib = [0, 1]
if N == 1:
    print(0)
elif N == 0:
    print(0)
else:
    for i in range (2, N):
        fib.append(fib[i-2] + fib[i-1])
    print(fib[N-1])