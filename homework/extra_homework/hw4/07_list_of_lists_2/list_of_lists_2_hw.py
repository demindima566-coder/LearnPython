nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

res1 = []
for i in nice_list:
    for j in i:
        for k in j:
            res1.append(k)

res2 = [i for j in nice_list for k in j for i in k]

print(res1)
print(res2)