# 글자 
lst = [list(input()) for _ in range(5)]
# 글자 수 
lst_length = [len(_) for _ in lst]

# 결과 저장
res = ""
for i in range(max(lst_length)):
    for j in range(5):
        try:
            res += lst[j][i]
        except:
            pass
print(res)