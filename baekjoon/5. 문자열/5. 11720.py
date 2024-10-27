# 풀이 1

s = input()
print(sum(map(int, input())))

# 풀이 2

s = input()
num = input()
total = 0

for i in num:
    total += int(i)
print(total)



# 풀이 3

s = input()
num = input()
total = 0

for i in range(s):
    total += int(num[i])
print(total)