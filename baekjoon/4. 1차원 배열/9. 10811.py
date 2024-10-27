n, m = map(int, input().split())
arr = [i for i in range(1,n+1)]
temp = 0

for _ in range(m):
    i, j = map(int, input().split())
    temp = arr[i-1:j]
    temp.reverse()
    arr[i-1:j] = temp
for _ in range(n):
    print(arr[_], end=" ")