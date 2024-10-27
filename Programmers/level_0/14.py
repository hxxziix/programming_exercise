# 더 크게 합치기

'''
연산 ⊕는 두 정수에 대한 연산으로 두 정수를 붙여서 쓴 값을 반환합니다. 
예를 들면 다음과 같습니다.
12 ⊕ 3 = 123
3 ⊕ 12 = 312
양의 정수 a와 b가 주어졌을 때, 
a ⊕ b와 b ⊕ a 중 더 큰 값을 return 하는 solution 함수를 완성해 주세요.

단, a ⊕ b와 b ⊕ a가 같다면 a ⊕ b를 return 합니다.
'''

a = 952
b = 91

def solution(a, b):
    answer = str(a)+str(b)
    res = str(b)+str(a)
    if int(answer) < int(res):
        return int(res)
    else:
        return int(answer)
print(solution(a, b))

# 풀이 2
def solution(a, b):
    return int(max(f"{a}{b}", f"{b}{a}"))
print(solution(a, b))

# 풀이 3
def solution(a, b):
    a, b = str(a), str(b)
    return int(max(a+b, b+a))
print(solution(a, b))