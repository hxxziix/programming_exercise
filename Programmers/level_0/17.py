# 공백수
'''
정수 number와 n, m이 주어집니다.
number가 n의 배수이면서 m의 배수이면 1을 아니라면 0을 
return하도록 solution 함수를 완성해주세요.
'''

number, n, m = map(int, input().split())
'''
def solution(number, n, m):
    if number % n == 0 and number % m == 0:
        return 1
    else: 
        return 0
print(solution(number, n, m))
'''

# 풀이 2
def solution(number, n, m):
    return int(number%n == 0 and number%m == 0)
print(solution(number, n, m))