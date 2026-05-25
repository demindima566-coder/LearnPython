lenght = int(input("Enter lenght of list: "))
nums = []
for i in range(lenght):
    if i % 2 == 0:
        nums.append(1)
    else:
        nums.append(i % 5)
print(f"Result: {nums}")