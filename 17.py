f = open('17.txt')
a = f.readlines()
a = list(map(int, a))

count = 0
m = 0
for i in range(len(a) - 1):
    if a[i] % 80 == 0 or a[i + 1] % 80 == 0:
        count += 1
        m = max(m, a[i] - a[i + 1])
print(count, m)