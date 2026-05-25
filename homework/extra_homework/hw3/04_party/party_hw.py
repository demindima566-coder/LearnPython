guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
while True:
    print(f"Сейчас на вечеринке {len(guests)} человек: {guests}")
    do = input("Гость пришёл или ушёл? ")
    if do == "Пора спать":
        print("Вечеринка закончилась, все легли спать")
        break
    name = input("Имя гостя: ")
    if do == 'пришёл':
        if len(guests) < 6:
            guests.append(name)
            print(f"Привет, {name}!")
        else:
            print(f"Прости, {name}, но мест нет.")
    elif do == "ушёл":
        guests.remove(name)
        print(f"пока, {name}!")
