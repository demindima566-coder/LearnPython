n = int(input("к-во эл-отв: "))
l = [int(input("введи число: ")) for _ in range(n)]
res = ""
for i in range(n - 1, -1, -1):
    if l[i] % 2 == 0:
        res += str(l[i]) + " "
print("чётные в обратном порядке:", res.strip())
#идём с конца и фильтруем