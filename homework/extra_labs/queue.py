class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def add(self, name):
        node = Node(name)
        if self.last is None:
            self.first = self.last = node
            print(name, " будет в начале очереди")
        else:
            self.last.next = node
            self.last = node
            print(name, "- добавлен в конец очереди")
        self.size += 1

    def delit(self):
        if self.first is None:
            print("Очередь пуста")
            return None
        person = self.first.data
        self.first = self.first.next

        if self.first is None:
            self.last = None
        self.size -= 1
        print(person, "- обслужен")
        return person

    def next_person(self):
        if self.first is None:
            return "Очередь пустая"

        return self.first.data

    def info(self):
        if self.first is None:
            print("Очередь пустая")
            return
        current = self.first
        print("Очередь: ")
        while current:
            print(current.data, end=' - ')
            current = current.next
        print("None")

    def kol(self):
        return self.size

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push_first(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

        if self.tail is None:
            self.tail = node

        self.size += 1
        print("Добавлено в начало:", value)

    def push_last(self, value):
        node = Node(value)
        if self.tail is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1
        print("Добавлено в конец:", value)

    def pop_first(self):
        if self.head is None:
            print("Deque пуст")
            return None

        item = self.head.data
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        self.size -= 1
        print("Удалено с начала:", item)
        return item

    def pop_last(self):
        if self.tail is None:
            print("Deque - пустой")
            return None

        if self.head == self.tail:
            item = self.tail.data
            self.head = self.tail = None
            self.size -= 1
            print("Удалено с конца: ", item)
            return item

        current = self.head

        while current.next != self.tail:
            current = current.next

        item = self.tail.data
        self.tail = current
        self.tail.next = None
        self.size -= 1
        print("Удалено с конца: ", item)
        return item

    def show(self):
        if self.head is None:
            print("Deque - пуст")
            return
        current = self.head
        print("Deque: ")

        while current:
            print(current.data, end=" - ")
            current = current.next
        print("None")
    def info(self):
        f = self.head.data if self.head else "None"
        l = self.tail.data if self.tail else "None"

        print("Начало: ", f)
        print("Конец: ", l)
        print("Размер: ", self.size)

q = Queue()
q.add("Ира")
q.add("Маша")
q.add("Артем")
q.add("Саша")

q.info()
print("Следующий:", q.next_person())
q.delit()
q.info()
print("Количество элементов:", q.kol())
print("Deque")
d = Deque()
d.push_first("A")
d.push_last("B")
d.push_first("X")
d.push_last("Y")
d.show()
d.info()

d.pop_first()
d.pop_last()

d.show()
d.info()