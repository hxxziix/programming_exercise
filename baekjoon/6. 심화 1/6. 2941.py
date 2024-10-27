lst = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

user = input()

empty = []
for i in lst:
    user = user.replace(i, "0")

print(len(user))