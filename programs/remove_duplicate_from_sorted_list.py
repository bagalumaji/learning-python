def remove_duplicate_sorted_list(lst):
    print(lst)
    l = len(lst)
    lp = 0
    rp = 1
    while rp < l:
        if lst[rp] != lst[rp - 1]:
            lp += 1
            lst[lp] = lst[rp]

        rp += 1

    return lp + 1


lst1 = [1, 2, 2, 3, 4, 4, 5]
l1 = remove_duplicate_sorted_list(lst1)
for i in range(0, l1):
    print(lst1[i])
