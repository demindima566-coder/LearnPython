skates, people = [], []

skates_kol = int(input("number of skates: "))
for i in range(skates_kol):
    size = int(input(f'Size pair number {i+1}: '))
    skates.append(size)
people_kol = int(input("Number of people: "))
for i in range(people_kol):
    size2 = int(input(f"Number {i+1}'s people foot size: "))
    people.append(size2)
skates.sort()
people.sort()

res = 0
skate_ind = 0
for p in people:
    while skate_ind < len(skates):
        if skates[skate_ind] >= p:
            res += 1
            skate_ind += 1
            break
        skate_ind += 1
print(f"The largest number of people who can take skates: {res}")