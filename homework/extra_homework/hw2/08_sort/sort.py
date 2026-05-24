n = int(input("к-во элементов: "))
l = [int(input("введи число: ")) for _ in range(n)]
for i in range(1, n):
    k = l[i]
    j = i - 1
    while j >= 0 and l[j] > k:
        l[j + 1] = l[j]
        j -= 1
    l[j + 1] = k
print("готовый список: ", l)
#сортировка вствками - сразу ставим новый элемент на правильное место