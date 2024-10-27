arr = [_+1 for _ in range(30)]

for _ in range(28):
    n = int(input())
    arr.remove(n)

print(min(arr))
print(max(arr))