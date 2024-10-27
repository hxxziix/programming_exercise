t = int(input())

for i in range(t):
    a, b = input().split()
    r = int(a)
    s = list(b)
    for 반복 in range(len(s)):
        print(s[반복] * r, end = "")
    print()

