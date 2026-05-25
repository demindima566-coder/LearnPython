text = input("Enter line: ")
fst = text.index("h")
lst = text.rindex("h")
rev = text[lst - 1:fst - 1]
print("Expanded sequence between first and last: ", rev)
#index - находит первое вхождение значения в скобках
#rindex - последнее