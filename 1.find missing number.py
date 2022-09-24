def fmn(n): #fmn = find missing number
    number = set(n)
    length = len(n)
    output = []
    for i in range(1, length + 1):
        if i not in number:
            output.append(i)
    return output
listofnumber = [1 , 2, 3, 4 ,6 ,7, 8, 9] 
print(fmn(listofnumber))