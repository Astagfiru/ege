def f(n):
    return int((oct(n)[2::] + '00'), 8)

def g(n):
    return int((oct(n)[2::]), 8)

n = int(f(100)) / int(g(100))
print(n)
#2330