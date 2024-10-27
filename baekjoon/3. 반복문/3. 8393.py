# 풀이 예제 1
n = int(input())
total = 0

for i in range(1, n+1) :
    total += i
print(total)



# 풀이 예제 2 (반복문 사용x)
print(sum(range(1, int(input())+1)))
