def f(x):
    a = 1
    while x > 0:
        a *= x % 11
        x = x // 11
    return a
x = 0
while f(x) != 140:
    x += 1
print(x)