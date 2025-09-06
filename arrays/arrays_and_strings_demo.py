
#       Arrays and Strings Demo
# ---------------------------------

#   Array Exercises
# Task 1

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

min = numbers[0]
max = numbers[0]
# Find min and max
for number in numbers:
    if number < min:
        min = number
    if number > max:
        max = number

print(f"Min: {min}, Max: {max}")

# Reverse the list
reversed_list = numbers[::-1]

print(f"Reversed List: {reversed_list}")

random_number = 7
# Check if random_number is in the list
if random_number in numbers:
    print(f"{random_number} is in the list.")
else:
    print(f"{random_number} is not in the list.")

# Calculate the sum of all elements
sum = 0
for number in numbers:
    sum += number
print(f"Sum: {sum}")


# Task 2

# Linear search function
def linear_search(num_list, target):
    if target in num_list:
        return num_list.index(target)
    return -1

target = 5
result = linear_search(numbers, target)
print("Result is ", result)


# Task 3

# Rotate the list to the right by 2 positions
for i in range(2):
    temp_num = numbers[-1]
    numbers.pop()
    numbers.insert(0, temp_num)

print("After rotating the list twice: ", numbers)


#   String Exercises
# Task 1

random_string = "PythonLearning"

# Access first and last character
print("First character: ", random_string[0])
print("Last character: ", random_string[-1])

# Slice the string to get "Learn"
print("Sliced string: ", random_string[6:11])

# Iterate through each character
for char in random_string:
    print(char, end=' ')
print()

# Check if "thon" is in the string
if 'thon' in random_string:
    print("'thon' is found in the string.")
else:
    print("'thon' is not found in the string.")

# Convert string to list of characters and back to string
random_string = list(random_string)
print("List of characters: ", random_string)
random_string = "".join(random_string)
print("Converted back to string: ", random_string)

# Task 2
# Reverse a string input by the user
user_input = input("Enter a string: ")
user_input = user_input[::-1]
print("Reversed string: ", user_input)

# Task 3
# Function to count vowels in a string
def vowels_count(input_string):
    count = 0
    vowels = 'aeiouAEIOU'
    for char in input_string:
        if char in vowels:
            count += 1
    return count

result = vowels_count(user_input)
print("Number of vowels: ", result)