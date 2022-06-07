import itertools
a = list(itertools.product('АБВГД', repeat = 5))

count = 0
for x in a:
    x = ''.join(x)
    if x[0] != 'А' and 'АА' not in x and 'ББ' not in x and 'ВВ' not in x and 'ГГ' not in x and 'ДД' not in x:
        print(x)
        count += 1
print(count)
#16385
