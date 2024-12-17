lst = [1,5,6,9,7,4,3,5,0,2,58,1,11,5,96,2]

# method 1
counts = {}

for item in lst:
    
    if item in counts:
        counts[item] += 1
        print()
    else:
        counts[item] = 1

print(counts)
print()

output: {1: 2, 5: 3, 6: 1, 9: 1, 7: 1, 4: 1, 3: 1, 0: 1, 2: 2, 58: 1, 11: 1, 96: 1}



# method 2

lst2 = [1, 2, 3, 4, 2, 5, 3, 6, 1]

counts2 = {}

for num in lst2:
    counts2[num] = counts2.get(num,0) +1

repeated_numbers = [num for num, count2 in counts2.items( ) if count2 >1]

print('repeated_numbers: ',repeated_numbers)

# outPut: repeated_numbers:  [1, 2, 3]



# method 3

lst3 = [1, 2, 3, 4, 2, 5, 3, 6, 1]

seen = set()
repeated_numbers = set()

for num in lst3:
    if num in seen:
        repeated_numbers.add(num)
    else:
        seen.add(num)

print('repeated_numbers3: ',list(repeated_numbers))

# outPut: repeated_numbers:  [1, 2, 3]