violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

kol = int(input("Сколько песен выбрать? "))
time = 0
for i in range(1, kol + 1):
    name = input(f"Название {i}-й песни: ")
    for n, d in violator_songs:
        if n == name:
            time += d
            break
print(f'Общее время звучания песен: {time} минуты')