num_lst = []        # 빈 리스트 생성

for i in range(9):  # for 반복문을 이용해 9번 입력받는 조건
    num_lst.append(int(input()))    # .append() 리스트 요소 추가 함수 이용해서 입력받기

print(max(num_lst))     # max() 함수를 통해 리스트 내 데이터 중 가장 큰 값 찾기
print(num_lst.index(max(num_lst))+1)    # index, max 함수를 이용해 가장 큰 값의 인덱스 찾고 +1 해줌 (인덱스번호 출력이 아닌 몇번 째인지 찾아야 함)