class Player:
    def make_ch(self):
        allowed = ["камень", "ножницы", "бумага"]
        ch = input((f"{self.name}, ходи: ")).lower().strip()
        while ch not in allowed:
            print("Ошибка! Введите: камень / ножницы / бумага")
            ch = input((f"{self.name}, ходи: ")).lower().strip()
        return ch

    def __init__(self, name):
        self.name = name
        self.score = 0

class Game:
    def delit(self):
        print("\n" * 50)

    def __init__(self):
        self.p1 = Player("игрок 1")
        self.p2 = Player("игрок 2")

    def get_winner(self, choice1, choice2):
        if choice1 == choice2:
            return None
        if choice1 == "камень" and choice2 == "ножницы":
                return self.p1
        if choice1 == "ножницы" and choice2 == "бумага":
            return self.p1
        if choice1 == "бумага" and choice2 == "камень":
            return self.p1
        return self.p2

    def play_round(self):
        print("Счет: ")
        print(self.p1.score, ":", self.p2.score)
        print("Ход игрока 1")
        ch1 = self.p1.make_ch()
        input("Нажмите Enter, чтобы продолжить")
        print("Ход игрока 2")
        ch2 = self.p2.make_ch()
        print("Результат: ")
        print(self.p1.name, " - ", ch1)
        print(self.p2.name, " - ", ch2)
        w = self.get_winner(ch1, ch2)
        if w is None:
            print("Ничья")
        else:
            w.score += 1
            print("Победил: ", w.name)
        print("Счет")
        print(self.p1.score, " - ", self.p2.score)

    def game(self):
        input("Нажми Enter чтобы начать")
        while (self.p1.score < 3) and (self.p2.score < 3):
            self.play_round()
            if (self.p1.score < 3) and (self.p2.score < 3):
                input("Нажми Enter для перехода к следующему раунду")
            self.delit()
        print("Конец игры")
        if self.p1.score == 3:
            print("Игрок 1 победил")
        else:
            print("Игрок 2 победил")

g = Game()
g.game()