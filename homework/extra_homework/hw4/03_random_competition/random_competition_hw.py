from random import uniform

t1 = [round(uniform(5,10), 2) for _ in range(20)]
t2 = [round(uniform(5,10), 2) for _ in range(20)]
n = []
for f, s in zip(t1, t2):
    n.append(max(f,s))
print(f'1st team: {t1}')
print(f'2nd team: {t2}')
print(f'Winners: {n}')
#uniform - случайное вещественное
#round - округление
#zip - соединяет элементы списка
#max - выбирает из двух