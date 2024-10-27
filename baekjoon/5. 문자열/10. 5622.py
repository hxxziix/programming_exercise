dial = ["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
input = input()

result = 0

for i in range(len(input)):
    for j in dial:
        if input[i] in j:
            result += dial.index(j)+3
print(result)