def f(N):
    n = bin(N)[2:-1]
    n += n[1] + n[1]
    return int(n, 2)

N = 4
while True:
    if f(N) > 76:
        print(N)
        break
    N += 1