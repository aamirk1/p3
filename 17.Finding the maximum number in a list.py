# Define a list of numbers
numbers = [10, 25, 7, 40, 12]
max_num = max(numbers)
second_max_num = max([num for num in numbers if num != max_num])
print("The second maximum number in the list is:", second_max_num)


# method 2

# Define a list of numbers
numbers = [10, 25, 7, 40, 12]

# Initialize variables to store the maximum and second maximum numbers
max_num = numbers[0]
second_max_num = float('-inf')  # Initialize with negative infinity

# Iterate through the list
for num in numbers:
    if num > max_num:
        second_max_num = max_num
        max_num = num
    elif num > second_max_num and num != max_num:
        second_max_num = num

# Print the result
print("The maximum number in the list is:", max_num)
print("The second maximum number in the list is:", second_max_num)




numbers = [10, 25, 7, 40, 12]
sorted_numbers = sorted(numbers)
second_max_num = sorted_numbers[-2]
print("The second maximum number in the list is:", second_max_num)



# Define a list of numbers
numbers = [10, 25, 7, 40, 12]

# Initialize a variable to store the maximum number
# Start by assuming the first element is the largest
max_num = numbers[0]

# Iterate through the list
for num in numbers:
    if num > max_num:
        max_num = num  # Update max_num if a larger number is found

# Print the result
print("The maximum number in the list is:", max_num)
