def calc(x,a, b):
    x = int(str(x), a)
    s = ''
    while x > 0:
        s += str(x % b)
        x //= b
    return s[::-1]

x = 81 * 15 + 3 * 22 - 27
x = calc(x, 10, 9)
m = str(x)
print(m.count('8'))