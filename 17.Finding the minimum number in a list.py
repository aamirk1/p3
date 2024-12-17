# Define a list of numbers
numbers = [10, 25, 7, 40, 12]

# Use the min() function to find the minimum number
min_num = min(numbers)

# Print the result
print("The minimum number in the list is:", min_num)




# method 2

# Define a list of numbers
numbers = [10, 25, 7, 40, 12]

# Initialize variables to store the minimum and second minimum numbers
min_num = numbers[0]
second_min_num = float('inf')  # Initialize with positive infinity

# Iterate through the list
for num in numbers:
    if num < min_num:
        second_min_num = min_num
        min_num = num
    elif num < second_min_num and num != min_num:
        second_min_num = num




# Print the result
print("The minimum number in the list is:", min_num)
print("The second minimum number in the list is:", second_min_num)



numbers = [10, 25, 7, 40, 12]
sorted_numbers = sorted(numbers)
second_min_num = sorted_numbers[1]
print("The second minimum number in the list using sorted is:", second_min_num)



# Define a list of numbers
numbers = [10, 25, 7, 40, 12]

# Initialize a variable to store the minimum number
# Start by assuming the first element is the largest
min_num = numbers[0]

# Iterate through the list
for num in numbers:
    if num < min_num:
        min_num = num  # Update min_num if a larger number is found

# Print the result
print("The minimum number in the list is:", min_num)
