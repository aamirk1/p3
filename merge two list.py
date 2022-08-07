def mtl(i ,j):
    mergelist = []
    while(i and j):
        if(i[0] <= j[0]):
            item = i.pop(0)
            mergelist.append(item)
        else:
            item = j.pop(0)
            mergelist.append(item)
    mergelist.extend(i if i else j)
    return mergelist
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]
print(mtl(list1 , list2))
