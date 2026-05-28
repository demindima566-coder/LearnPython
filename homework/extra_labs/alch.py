class Block:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Craft:
    def __init__(self):
        self.items = {}
        self.recipies = {}
        self.add_all_recipes()
        self.start_items()

    def add_recipe(self, a, b, result):
        self.recipies[(a, b)] = result
        self.recipies[(b, a)] = result

    def start_items(self):
        self.items["дерево"] = Block("дерево")
        self.items["камень"] = Block("камень")
        self.items["уголь"] = Block("уголь")
        self.items["железо"] = Block("железо")

    def add_all_recipes(self):
        self.add_recipe("дерево", "камень", "кирка")
        self.add_recipe("дерево", "уголь", "факел")
        self.add_recipe("железо", "уголь", "сталь")
        self.add_recipe("камень", "железо", "меч")
        self.add_recipe("кирка", "железо", "алмаз")
        self.add_recipe("меч", "огонь", "огненный меч")
        self.add_recipe("факел", "дерево", "костер")

    def show_items(self):
        print("Предметы")
        for i in sorted(self.items):
            print('', i)
        print("Всего предметов: ", len(self.items))

    def craft(self, first, second):
        first = first.lower()
        second = second.lower()

        print("Крафт: ", first, "+", second)
        if first not in self.items:
            print("Предмет ", first, " не найден")
            return None
        if second not in self.items:
            print("Предмет ", second, "  не найден")
            return None
        if (first, second) not in self.recipies:
            print("Крафт невозможен")
            return None

        res = self.recipies[(first, second)]
        if res in self.items:
            print("Предмет", res, "уже открыт")
        else:
            self.items[res] = Block(res)
            print("Получен предмет: ", res)
        return res

g = Craft()
g.show_items()
g.craft("дерево", "камень")
g.craft("дерево", "уголь")
g.craft("железо", "уголь")
g.craft("камень", "железо")
print("Крафт")
g.craft("кирка", "железо")
g.craft("факел", "дерево")
print("")
g.craft("дерево", "камень")
g.show_items()