#первая версия, написал в классе

def input_players():
    print("Введите количество игроков")
    num_of_players = int(input())

    print("Введите символы: камень / ножницы / бумага")

    mas = []
    allowed = {"камень", "ножницы", "бумага"}

    for i in range(1, num_of_players + 1):
        cim_i = input().strip().lower()

        while cim_i not in allowed:
            print("Ошибка. Введите только: камень / ножницы / бумага")
            cim_i = input().strip().lower()

        print("Игрок", i, "ввел", cim_i)
        mas.append(cim_i)

    return mas


def matching(moves):
    unique_moves = set(moves)

    if len(unique_moves) == 1 or len(unique_moves) == 3:
        return "ничья"

    if "камень" in unique_moves and "ножницы" in unique_moves:
        winning_move = "камень"
    elif "ножницы" in unique_moves and "бумага" in unique_moves:
        winning_move = "ножницы"
    else:
        winning_move = "бумага"

    winners = []

    for i in range(len(moves)):
        if moves[i] == winning_move:
            winners.append(i + 1)

    return winners


def print_result(result):
    if result == "ничья":
        print("Ничья")
    else:
        print("Победили игроки:", *result)



mas = input_players()
result = matching(mas)
print_result(result)