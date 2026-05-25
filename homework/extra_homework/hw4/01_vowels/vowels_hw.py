text = input("Enter text: ").lower()
vowels = 'ауоыиэяюёе'
res = []
for letter in text:
    if letter in vowels:
        res.append(letter)
print(f'List of vowels: {res}')
print(f'Length of list: {len(res)}')