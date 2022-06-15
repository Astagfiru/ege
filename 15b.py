def f(x, y):
    a = bin(x)[2::]
    b = bin(y)[2::]
    if len(a) < len(b):
        a = "0" * (len(b) - len(a)) + a
    else:
        b = "0" * (len(a) - len(b)) + b
    res = ''
    for i in range(len(b)):
        res += str(int(a[i]) * int(b[i]))
    return int(res)


A = 1
while True:
    for x in range(0, 1000):
        if not(f(x,33) == 0 <= (f(x,45) != 0 <= f(x,A) != 0)):
            break
    else:
        print(A)
    A += 1