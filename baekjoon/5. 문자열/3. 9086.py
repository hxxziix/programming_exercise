t = int(input())

for i in range(t):
    s = input()
    print(f"{s.strip()[0]}{s.strip()[-1]}") # 방법 1
    print(f"{s[0]}{s[-1]}")                 # 방법 2
