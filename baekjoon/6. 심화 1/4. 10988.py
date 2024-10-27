s = input()
r_s = ""
for i in reversed(s):
    r_s += i

if s == r_s:
    print("1")
else:
    print("0")