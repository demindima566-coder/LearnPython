text = input("Enter message: ")
bias = int(input("Enter bias "))
alph = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
res = ''
for l in text:
    if l in alph:
        i1 = alph.index(l)
        i2 = (i1 + bias) % len(alph) #как rhyme_cnt на случай вылета за круг
        res += alph[i2]
    else:
        res += l
print("Caesar ciper: ", res)