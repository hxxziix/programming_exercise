count = 0
mx = 0
lis = list()

for i  in range(9):
    lis = list(map(int, input(). split('\n')))
    if mx < max(lis):
        mx = max(lis)
        count = max(lis.index())

print(mx)
print(count)