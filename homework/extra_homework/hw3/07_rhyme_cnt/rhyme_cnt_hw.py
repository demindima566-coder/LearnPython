people_kol = int(input("Number of people: "))
n = int(input("What number is in rhyme "))
people = list(range(1, people_kol + 1))
current_ind = 0
print(f"Every {n} person is eliminated ")
while len(people) > 1:
    current_ind %= len(people)#в случай вылета за предел круга, возвращаемся на нужный индекс
    print(f"Current number of people: {people}")
    print(f"Start with number {people[current_ind]}")
    current_ind = (current_ind + n - 1) % len(people)
    eliminated = people.pop(current_ind)
    print(f"Person number {eliminated} leaves ")
print(f"Person number {people[0]} win ")