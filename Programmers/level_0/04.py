# 대소문자 바꿔서 출력하기

str = input()
res = []

for s in str:
    if s.isupper():
        res.append(s.lower())
    elif s.islower():
        res.append(s.upper())
result = "".join(res)
print(result)