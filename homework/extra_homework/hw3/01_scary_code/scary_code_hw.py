main = [1, 5, 3]
pb1 = [1, 5, 1, 5]
pb2 = [1, 3, 1, 5, 3, 3]

main.extend(pb1)
count1 = main.count(5)
print(count1)

while 5 in main:
    main.remove(5)

main.extend(pb2)
count2 = main.count(3)
print(count2)

#while 3 in main:
#    main.remove(3)

print(main)