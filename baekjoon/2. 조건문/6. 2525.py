h,m = map(int, input().split())
timer = int(input())

h += timer // 60
m += timer % 60

if m >= 60 :
    m -= 60
    h += 1
if h >= 24 :
    h -= 24


print(f'{h} {m}')