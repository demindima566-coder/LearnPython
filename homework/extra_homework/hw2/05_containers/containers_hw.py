n = int(input("к-во контейнеров: "))
ves1 = [int(input("введи вес контейнера: ")) for _ in range(n)]
ves2 = int(input("/n введи вес нового контейнера: "))
pos = len([w for w in ves1 if w >= ves2]) + 1
print(pos)