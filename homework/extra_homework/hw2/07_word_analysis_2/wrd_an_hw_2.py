word = input("введи слово: ").lower().strip()
if word == word[::-1]:
    print("палиндром")
else:
    print("не очень палиндром")