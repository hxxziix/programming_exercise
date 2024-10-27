h,m = map(int, input().split())

if h > 0 and m < 45 :
    h = h -1
    m = 60 - (45 - m)
    print(f'{h} {m}')
elif h <= 0 and m < 45 :
    h = 23
    print(f"{h} {60 - (45 - m)}")
else :
    print(f'{h} {m - 45}')
