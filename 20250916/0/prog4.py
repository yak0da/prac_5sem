n = 0
res = 0
while (a := int(input())) != 0:
    n += 1
    if a == n:
        res += 1
print(res)