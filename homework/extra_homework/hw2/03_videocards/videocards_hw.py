n = int(input("к-во карт: "))
vk = [int(input(f"{i + 1} карта: "))for i in range(n)]
print("/n список старых карт: ", vk)
nvk = [x for x in vk if x!= max(vk)]
print("новый список карт", nvk)