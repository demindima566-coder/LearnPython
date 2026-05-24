n = int(input("к-во элементов: "))
l = [int(input("введи элемент: "))for _ in range(n)]
k = int(input("сдвиг: "))
k %= n
res = l[-k:] + l[:-k]
print("до: ", l)
print("после: ", res)