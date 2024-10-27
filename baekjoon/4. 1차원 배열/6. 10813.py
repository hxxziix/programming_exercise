n, m = map(int, input().split())        # 입력

lst = [a +1 for a in range(n)]          # 1~5 까지 배열

for _ in range(m):                      # 반복문을 통해 바꿀 위치 입력받기
    i, j = map(int, input().split())
    
    a = lst[i-1]                        # 입력받은 값 바꿔주기
    lst[i-1] = lst[j-1]
    lst[j-1] = a

for a in lst:                           # 반복문을 통해 출력함
    print(a, end = " ")