list1 = [1, 2, 3, 6, 8, 10]
list2 = [4, 4]

#v1
def merge_sorted_lists_1(list1, list2):
    merged = sorted(set(list1 + list2))
    return merged


#v2 зная, что списки отсортированы
def merge_sorted_lists_2(list1, list2):
    merged = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            n = list1[i]
            i += 1
        elif list1[i] > list2[j]:
            n = list2[j]
            j += 1
        else:
            n = list1[i]
            i += 1
            j += 1
        if n not in merged:
            merged.append(n)
    while i < len(list1):
        if list1[i] not in merged:
            merged.append(list1[i])
        i += 1
    while j < len(list2):
        if list2[j] not in merged:
            merged.append(list2[j])
        j += 1
    return merged

print(merge_sorted_lists_1(list1, list2))
print(merge_sorted_lists_2(list1, list2))