PYTHON QUIZ # 2

# This is an open book test. You may use the internet to assist with your answers- NO PHONES ALLOWED!
# You will have the entire class time to complete your quiz. It must be submitted before class is over to recieve a grade.
# Take your time, read the questions thoroughly, find context clues and keywords to help you. 

# GOOD LUCK!
#-----------------------------------------------------------------------------------------------------------#

# 1. Create a function that will multiply two (2) values that are passed into the function as arguments. 
# Your function should print out the result of the two numbers that have been multiplied.

def multiply_numbers(x, y):
    result = x * y
    print(f"The result of multiplying {x} and {y} is: {result}")

# Call the function with two values
value1 = float(input("Enter the first value: "))
value2 = float(input("Enter the second value: "))

multiply_numbers(value1, value2)

# 2. Creat a function that will do the following calculation. Your function should take in three argument. it should add the first
# two arguments and then the sum of the first two (2) should be divided by the third argument. 
# You function should then print the result. 


You can create a Python function that takes three arguments, adds the first two, and then divides the sum by the third argument. Here's an example:

python
Copy code
def calculate_and_divide(x, y, z):
    sum_of_first_two = x + y
    result = sum_of_first_two / z
    print(f"The result of ({x} + {y}) / {z} is: {result}")

# Call the function with three values
value1 = float(input("Enter the first value: "))
value2 = float(input("Enter the second value: "))
value3 = float(input("Enter the third value: "))

calculate_and_divide(value1, value2, value3)

# 3. Create a elevator function that will run specific lines of code based on the conditions provided by a user. If the user types in 101,
# the function should print out they are going to the boys latin office, if they type in 203, they are going to the gym, 
# and if they type in the letter g, the lobby. else, if the input doesnt match any of the values provided, tell the user that floor doesn't exist and to please
# enter a valid floor number.

# hint you will need to look into using conditional statements

def elevator(floor):
    if floor == "101":
        print("You are going to the Boys Latin office.")
    elif floor == "203":
        print("You are going to the gym.")
    elif floor == "g":
        print("You are going to the lobby.")
    else:
        print("Floor doesn't exist. Please enter a valid floor number.")

# Get the floor input from the user
floor_input = input("Enter the floor number: ")

# Call the elevator function with the user's input
elevator(floor_input)

# 4. Write a simple conditional statement that uses a boolean that will print if it is daytime or nighttime.

is_daytime = True  # Change this boolean value to test different conditions

if is_daytime:
    print("It is daytime.")
else:
    print("It is nighttime.")

# 5. What function would you use if you wanted to add and element/ value to a list data type? Explain why you would use it.

my_list = [1, 2, 3, 4]
new_element = 5
my_list.append(new_element)

# 6. Do some research and find the correct built-in python function that will reverse the order of the following list.
# then print your list in the reverse order.

random_number_list = [0,1,2,3,4,5,6,7,8]

random_number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# Reverse the list in place
random_number_list.reverse()

# Print the reversed list
print(random_number_list)

reversed_list = random_number_list[::-1]

# Print the reversed list
print(reversed_list)
#
#  7.Do some research and find the correcrt built-in python function that will allow you to find the largest number in the following list.
# then print the largest number

ranom_number_list2 = [100,230,40,39403,19]

random_number_list2 = [100, 230, 40, 39403, 19]

# Find and print the largest number in the list
largest_number = max(random_number_list2)
print("The largest number is:", largest_number)


# 8. A security company has hired you as an engineer to help them develop a program that will only let users into the building 
# if they enter a specific password. They given you the following information to use to build this program.
# - they want users to be able to enter a series of codes to get access
# - they want the user to enter an initial password value which is 0001
# - if they get this correct, they then want them to enter another value, which is 3039
# - if this is correct they will get access to the building
# - if they have the wrong answer in either scenario they will get a message saying access denied. 

# Define the correct passwords
initial_password = "0001"
secondary_password = "3039"

# Ask the user to enter the initial password
user_initial_password = input("Enter the initial password: ")

# Check the initial password
if user_initial_password == initial_password:
    # If the initial password is correct, ask for the secondary password
    user_secondary_password = input("Enter the secondary password: ")
    
    # Check the secondary password
    if user_secondary_password == secondary_password:
        print("Access granted. You can enter the building.")
    else:
        print("Access denied. Secondary password is incorrect.")
else:
    print("Access denied. Initial password is incorrect.")

# 9. What does it mean to call a function? Why do we call functions. 
# you can use the variable below to enter you ansewer. 
answer9='your answer here'


Calling a function in programming means invoking or executing that function to perform a specific set of tasks or actions defined within the function. Functions are blocks of code that encapsulate a particular task or a set of tasks, and they are designed to be reusable. Here's why we call functions:

1. **Modularity and Reusability:** Functions allow us to break down a complex program into smaller, more manageable parts. These parts can be reused in different parts of the program and in different programs altogether. Instead of writing the same code multiple times, we call the function wherever we need that functionality.

2. **Abstraction:** Functions hide the implementation details of a task. When calling a function, we don't need to know how it accomplishes the task; we only need to know what it does and how to use it. This abstraction simplifies code and makes it easier to understand.

3. **Parameterization:** Functions can accept input parameters (arguments) that allow us to customize their behavior. Parameters provide flexibility and enable the function to work with different data or perform different variations of the same task.

4. **Organization:** Functions help organize code into logical, reusable, and self-contained units. This improves code readability and maintainability, as it's easier to locate and modify specific functionality within a program.

5. **Code Clarity:** Functions enhance code clarity by giving meaningful names to specific operations or tasks. This makes the code more self-documenting and easier to read.

In summary, calling functions is a fundamental aspect of programming that enables code reuse, organization, and abstraction. We call functions to perform specific tasks or operations, encapsulated within those functions, which makes our code more modular, readable, and maintainable.



# 10. Find and print each value at the specific indexes provided in the list.
# find and print the values/words at index 3, 4, and 6 

shopping_cart = ['apples','water','chicken','ice cream','ground beef','string beans','oranges']

shopping_cart = ['apples', 'water', 'chicken', 'ice cream', 'ground beef', 'string beans', 'oranges']

# Find and print values at specific indexes
index_3 = shopping_cart[3]
index_4 = shopping_cart[4]
index_6 = shopping_cart[6]

print("Value at index 3:", index_3)
print("Value at index 4:", index_4)
print("Value at index 6:", index_6)
                                            `````````````qqqqqazszxzxszasawqqazzxsq12334`