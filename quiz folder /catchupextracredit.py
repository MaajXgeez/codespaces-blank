# 1. Identify 4 different data types and provide a 
# use case/ scenario for when you would use each one.

Certainly! Here are four different data types and their respective use cases/scenarios:

1. **Integer (int):**
   - **Use Case/Scenario:** You would use the integer data type to represent whole numbers in programming. For example, when tracking the quantity of items in a shopping cart, the age of a person, or the number of days in a month, you would use integers.

2. **Floating-Point (float):**
   - **Use Case/Scenario:** Floating-point numbers are used to represent values with a fractional part. For instance, when dealing with measurements like temperature (e.g., 98.6°F), currency (e.g., $19.99), or scientific data (e.g., 3.14159 for π), you would use floating-point data types.

3. **String (str):**
   - **Use Case/Scenario:** Strings are used to store text data. You would use strings to represent names, addresses, messages, and any sequence of characters. For example, when storing a person's name like "John Smith" or a message like "Hello, World!", you would use string data types.

4. **Boolean (bool):**
   - **Use Case/Scenario:** Booleans are used for representing binary values, typically "True" or "False." They are essential for making decisions in conditional statements. For example, when checking if a user is logged in (True) or not (False) to grant access to certain features, you would use boolean data types.

These are just a few examples of data types, and programming languages often have more specialized data types to handle various scenarios and data structures.


# 2. Describe what a variable is and also provide 
# three (3) variable naming rules

**Variable Definition:**
A variable is a symbolic name or identifier used to store and manipulate data within a computer program. It acts as a container or a storage location in the computer's memory where you can store and retrieve values. Variables are fundamental components of programming and are used to store various types of data, such as numbers, text, and complex objects.

**Three Variable Naming Rules:**

1. **Start with a letter or underscore:** Variable names must begin with a letter (a-z, A-Z) or an underscore (_) character. It should not start with a number (0-9) or any other special character.

2. **Consist of letters, numbers, and underscores:** Variable names can include letters, numbers, and underscores. They are case-sensitive, meaning that uppercase and lowercase letters are considered different. For example, "myVariable" and "myvariable" would be treated as distinct variables in most programming languages.

3. **Avoid using reserved words:** Variable names should not be the same as reserved words or keywords in the programming language you are using. Reserved words have special meanings and are used for specific purposes within the language. For example, in Python, you should avoid naming a variable "if," "while," or "class" because these are reserved keywords.

Following these naming rules ensures that your variables are easy to understand and maintain, making your code more readable and less error-prone. Additionally, it's a good practice to use descriptive and meaningful names for your variables to enhance the clarity of your code.

# 3. **Variable Definition:**
A variable is a symbolic name or identifier used to store and manipulate data within a computer program. It acts as a container or a storage location in the computer's memory where you can store and retrieve values. Variables are fundamental components of programming and are used to store various types of data, such as numbers, text, and complex objects.

**Three Variable Naming Rules:**

1. **Start with a letter or underscore:** Variable names must begin with a letter (a-z, A-Z) or an underscore (_) character. It should not start with a number (0-9) or any other special character.

2. **Consist of letters, numbers, and underscores:** Variable names can include letters, numbers, and underscores. They are case-sensitive, meaning that uppercase and lowercase letters are considered different. For example, "myVariable" and "myvariable" would be treated as distinct variables in most programming languages.

3. **Avoid using reserved words:** Variable names should not be the same as reserved words or keywords in the programming language you are using. Reserved words have special meanings and are used for specific purposes within the language. For example, in Python, you should avoid naming a variable "if," "while," or "class" because these are reserved keywords.

Following these naming rules ensures that your variables are easy to understand and maintain, making your code more readable and less error-prone. Additionally, it's a good practice to use descriptive and meaningful names for your variables to enhance the clarity of your code.

# 4. Create a function that will prompt a user to enter their name and their grade 
# and depending on their grade level will return a custom message. If the user is in 
# grades 9 and 10, The message should be as followed:
# Welcome “student name” to ‘introduction to Python’ class.
# Else if they are in grades 11 or 12, the message should be the following:
# Welcome “student name” to Advance Placement Python’ class


def welcome_message():
    name = input("Enter your name: ")
    grade = int(input("Enter your grade: "))

    if grade in [9, 10]:
        message = f"Welcome {name} to 'Introduction to Python' class."
    elif grade in [11, 12]:
        message = f"Welcome {name} to 'Advance Placement Python' class."
    else:
        message = f"Sorry, we don't have a Python class for your grade."

    return message

# Call the function to display the welcome message
print(welcome_message())


# 5. Write a program that will apply a discount to a person's purchase, 
# only if they are a member of the store’s club. Your function should allow a user to 
# enter a product name and product price. The product price should be entered as a float. 
# Your program should ask the user if they are a member of their stores club. If yes, 
# then apply a 25% discount to their product and return the final price of the item. If no, 
# ask the user if they would like to become a member. If the user enters yes, they will receive a 
# 10% discount on their product. If the user enters no, they do not want to become a member, your program 
# should return the regular price of the item. 


def apply_discount():
    product_name = input


# 6. Create a program that will loop through an array of lists to find all the users who are members of the math club. 
# Use the following array of lists below:

john=['john','10th grade','math club']
jennie=['jennie','11th grade','basketball']
april=['april','12th grade','football']
may= ['may','9th grade','math club']
robert=['robert','11','math club']

students=[john, jennie, april,may, robert]


# Define the list of students
john = ['john', '10th grade', 'math club']
jennie = ['jennie', '11th grade', 'basketball']
april = ['april', '12th grade', 'football']
may = ['may', '9th grade', 'math club']
robert = ['robert', '11', 'math club']

students = [john, jennie, april, may, robert]

# Initialize an empty list to store math club members
math_club_members = []

# Loop through the students and check if they are in the math club
for student in students:
    if 'math club' in student:
        math_club_members.append(student[0])

# Display the list of math club members
print("Math Club Members:")
for member in math_club_members:
    print(member)


# 7. Create a program that uses a combination of at least three (3) concepts 
# we've learned about in class.

# Initialize an empty list to store tasks
tasks = []

# Main menu for task management
while True:
    print("Task Manager Menu:")
    print("1. Add a task")
    print("2. List tasks")
    print("3. Mark task as complete")
    print("4. Quit")
    
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == "1":
        task_name = input("Enter the task name: ")
        task = {"name": task_name, "completed": False}
        tasks.append(task)
        print(f"Task '{task_name}' added to the list.")
    
    elif choice == "2":
        if not tasks:
            print("No tasks in the list.")
        else:
            print("Tasks:")
            for index, task in enumerate(tasks, start=1):
                status = "Completed" if task["completed"] else "Incomplete"
                print(f"{index}. {task['name']} - {status}")
    
    elif choice == "3":
        if not tasks:
            print("No tasks to mark as complete.")
        else:
            task_index = int(input("Enter the task number to mark as complete: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["completed"] = True
                print(f"Task '{tasks[task_index]['name']}' marked as complete.")
            else:
                print("Invalid task number.")
    
    elif choice == "4":
        print("Task Manager is quitting. Goodbye!")
        break

    else:
        print("Invalid choice. Please choose a valid option (1/2/3/4).")
