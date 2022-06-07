def f(N):
    n = bin(N)[2:]
    n += str(sum(map(int, n)) % 2)
    n += str(sum(map(int, n)) % 2)
    return int(n, 2)

N = 1
m = float('inf')
while True:
    if f(N) > 97:
        m = min(m, f(N))
        print(m)
    N += 1