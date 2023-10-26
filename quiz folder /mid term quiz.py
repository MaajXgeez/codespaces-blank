# 1. Describe what a computer program is and what does it do. 

a set of ordered operations that a computer must complete
# 
# 
# 2. Describe what complexitity and abstraction are, then provide an example
# of complexity in the real world and how we apply abstraction to that thing (you example must be original and cannot be an example
# used in our lecture slides ie car, grocery store, etc.). 

a foundational idea in software engineering that enables programmers to control system complexity by emphasizing key components and concealing unimportant elements.
  
# 3. What is Syntax in Python and why is it important to write proper syntax?
the collection of guidelines that specify the format and interpretation of a Python program
# 
# 4.  What is a function, and why do we wrap our code inside of functions?

group the code  and give it a name so  we can call it by that name later


# 5.  Name and describe the three (3) naming conventions for variables in python? Then provide three (3) name rules for Python
# variables. 

1. **Snake Case:** 
   - `my_variable`
   - `user_name`
   - `total_count`

2. **Camel Case:** 
   - `myVariable`
   - `userName`
   - `totalCount`


3. **Pascal Case:** 
   - `MyClass`
   - `PersonInfo`
   - `TotalCount`

**Variable Name Rules:**

# 6. What will be the output of the print functons when this code is ran, explain why
name = 'Bill'
student = name
name = 'Walter'
student= 'Richard'

print(name)
print(student)

Walter
Richard



# 7. Describe the difference between each of the following assignment operators:
# = 
# ==
# !=
 


1. '=' (Assignment Operator):
   - The '=' operator is used to assign a value to a variable.
   - It takes the value on the right side of the operator and assigns it to the variable on the left side.
   - Example: `x = 5` assigns the value 5 to the variable 'x', replacing any previous value it had.

2. '==' (Equality Operator):
   - The '==' operator is used to compare two values to check if they are equal.
   - It returns a boolean value, 'True' if the values are equal, and 'False' if they are not.
   - Example: `x == 5` checks if the value of 'x' is equal to 5 and returns 'True' if it is, or 'False' if it isn't.

3. '!=' (Inequality Operator):
   - The '!=' operator is used to compare two values to check if they are not equal.
   - It returns a boolean value, 'True' if the values are not equal, and 'False' if they are equal.
   - Example: `x != 5` checks if the value of 'x' is not equal to 5 and returns 'True' if they are different, or 'False' if they are the same.

In summary, '=' is used for assignment, '==' is used to test equality, and '!=' is used to test inequality. It's essential to use the correct operator for the specific operation you intend to perform in your code.

   
# 8. What type of data can be stored in a python list?

; int, float, etc., and also more advanced Python types,

# 9. Create a function that will take in a word provided by a user and then output that word back to the user but in reverse. 


def reverse_word(word):
    reversed_word = word[::-1]
    return reversed_word

# Get input from the user
user_input = input("Enter a word: ")

# Call the function and print the reversed word
reversed = reverse_word(user_input)
print("Reversed word:", reversed)
 

 
# 10. Create three (3) seperate functions that will do addition, subtraction, and multiplication respectively. 
# each of these functions should take two (2) arguments. When the user passes these arguments into the function, they will be
# calculated together and return the output in your terminal. 



def add(x, y):
    result = x + y
    return result

# Example usage:
# result = add(5, 3)
# print(result)  # Output: 8

def subtract(x, y):
    result = x - y
    return result

# Example usage:
# result = subtract(10, 4)
# print(result)  # Output: 6

def multiply(x, y):
    result = x * y
    return result

# Example usage:
# result = multiply(6, 7)
# print(result)  # Output: 42





# 11. What is the difference between a function argument and a function parameter. 
Function Parameter:

Parameters are the placeholders or variables that you define in a function's signature or definition.
They are like local variables within the function and act as receptacles for the values passed as arguments when the function is called.
Parameters are used to specify what kind of input the function expects and may have default values or data types specified.
Example:

python
Copy code
def greet(name):
    print(f"Hello, {name}!")

# Here, 'name' is a parameter of the 'greet' function.
Function Argument:

Arguments are the actual values or expressions that you provide when calling a function.
These values are passed into the function to be used with the corresponding parameters.
The function performs its operations on these argument values, which can be different each time the function is called.
Example:

python
Copy code
greet("Alice")

# Here, "Alice" is an argument passed to the 'greet' function.
In summary, parameters are defined within the function's signature and act as placeholders for the values you pass as arguments when calling the function. Arguments are the actual values or expressions you pass to the function during the function call. The parameter receives and works with the values provided as arguments.








# 12. You have been hired by a software company and your first assignment is to develop a password authenticator program. 
# the goal of your program is to check a user's password and make sure it meets the company's password requirements. 
# the company has provided you with the following requirements for the passcode program:
# a. the passcode must NOT contain any numbers
# b. the passcode must NOT contain any capital letters
# c. the passcode can NOT be any longer than five (5) characters
# d. the passcode can NOT shorter the three (3) characters
# e. the user should be able to enter their password and if it meets the requirements, should print a message saying that 
# their password was created successfully, and if it was not, should send back a message with one of the following issues. 

def is_valid_password(password):
    # Check if the password is between 3 and 5 characters in length.
    if len(password) < 3 or len(password) > 5:
        return "Password must be between 3 and 5 characters."

    # Check if the password contains any digits (numbers).
    if any(char.isdigit() for char in password):
        return "Password cannot contain numbers."

    # Check if the password contains any capital letters.
    if any(char.isupper() for char in password):
        return "Password cannot contain capital letters."

    # If all checks pass, the password is valid.
    return "Password created successfully."

# Get the user's password as input.
user_password = input("Enter your password: ")

# Check the validity of the user's password.
result = is_valid_password(user_password)

# Display the result to the user.
print(result)





# 13. When you run your code and see typeError in your terminal, what does that typically mean and how would you try to solve
# the issue?

Read the Error Message: The TypeError message will provide important information about the issue. It usually includes details about the operation that caused the error and the data types involved.

Identify the Problem: Look at the code line where the error occurred and identify which variable or expression is causing the problem.

Check Data Types: Ensure that you are using the correct data types for the intended operation. For example, if you are trying to perform arithmetic, make sure you are working with numbers, not strings.

Verify Variable Values: Check the values of variables involved in the operation. If you expect a variable to have a certain data type or value, make sure it meets those expectations.

Check Function Arguments: If the error occurs in a function call, review the function's signature (parameters) and how you are passing arguments to it. Ensure that the arguments match the expected data types.

Inspect Loops and Iterations: If you're working with loops, ensure that the loop variables and the values they iterate over are of the correct types.

Consider Type Conversions: In some cases, you may need to convert data types explicitly using functions like int(), str(), or others.

Use Print Statements: Insert print statements to help you debug and see the values of variables or expressions at different stages of the code.

Check for Typos: Typographical errors, such as using the wrong variable name or misspelling a function, can also lead to TypeError. Double-check your code for typos.

Review Documentation: If you're using external libraries or functions, consult their documentation to ensure you are using them correctly.

Test Incrementally: If you suspect a particular part of your code is causing the error, comment out or isolate that portion and test it separately.

Seek Help: If you can't resolve the issue on your own, consider seeking help from online communities, forums, or colleagues who may have experience with similar problems.

Use Debugging Tools: Utilize debugging tools provided by your programming environment to step through the code and identify the source of the error.

By following these steps and carefully analyzing the error message, you can typically identify and resolve TypeError issues in your code.








# 14. When you run your code and see indentError in your terminal, what does that typically mean and how would you try to solve 
# the issue?

# 15. Create a while loop that check a user's password. If they enter the password correct, they will get a message saying 
# that the password was entered successfully. If they enter the password incorrectly, it will tell the user to try again. 
# The user should only have three (3) attempts to get the password correct. If they enter the password incorrect on the fourth 
# attempt, a message should appear telling them that have been locked out and need to talk to the administrator. 

# 16. Which item is at index 5
giftShopping=['xbox','sneakers','necklace','clothing','laptop','gift card']

# 17. Create a for loop that will print ONLY the even numbers within the range of the variable provided below.
# HINT: You will need to use the range() function. 
upToNumber = 30

# 18. Create a function that uses a conditional statement that checks if a person qualifies for a raise on their salary. 
# The user should be able to enter their name, their salary (how much money they make in an entire year), and how long they have
# worked at the company. If the user has been working at the company longer than four (4) years, they will get a 15% raise. 
# Your program should be able to calculate what their salary is with the 15% increase. If the user qualifies, your program
# should return the a message congratulating the user by name, and telling them what their new salary is with the 15%
# increase (this must be the actual number). If they do not qualify inform the user that unfortunately they do not qualify. 

# 19. Create a function that checks which value is greater than the other. Your function should take two (2) integer parameters. 
# and should evaluate which number is larger. Your function should then print the largest number. 

# 20. Create a while loop function that will add gift items to a list. Your function should ask the user to enter an item name. 
# The item name should then be added to a list variable called gift_bag. Your gift bag should have a limit of six (6) items. 
# Once your gift bag hits its limit of six (6) items your program should print a message saying 
# that the gift bag is full and print the list of items in the gift bag.   
 


 