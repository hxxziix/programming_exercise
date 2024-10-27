n = int(input())
list = []
for i in range(n) :
    list = map(int, input().split())
    
v = int(input())

a = list.count(v)
print(a)