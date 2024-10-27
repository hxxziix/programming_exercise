lst = [list(map(int, input().split())) for _ in range(9)]

res = 0
max_col, max_low = 0, 0

for low in range(9):
    for col in range(9):
        if res <= lst[low][col]:
            max_low = low + 1 
            max_col = col + 1
            res = lst[low][col]
print(res)
print(max_low, max_col)