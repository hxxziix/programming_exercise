n = int(input())
i_score = list(map(int, input().split()))
max_score = max(i_score)

arr = []
for i in i_score:
    arr.append(i / max_score * 100)

print(sum(arr) / n)
