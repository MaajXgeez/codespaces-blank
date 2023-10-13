
# 1. Provided below is some starter code. 
# Fix this code to create a loop that will iterate
# until it gets to the number 10.

# hint: remember there are 3 parts to a loop. 
i=0
while i # insert missing code.
    print('insert missing value')
    # insert missing code here
    

    i = 0
while i < 10:  # This is the missing code to specify the condition for the loop
    print('insert missing value')
    i += 1  # This is the missing code to update the value of i


# 2. Create a simple while loop that will iterate over a the following condition:
# The loop will ask the user to enter the secret number. The secret number is 3. 
# If the user enters the secret number correctly, the loop will stop and tell the user
# the can win a prize. 
# If the user puts in an incorrect secret number, the loop will ask them to enter the 
# correct secret number. 

# 3. describe the difference between a while loop and a conditional statement. 
# Try be as specific as you can

secret_number = 3  # The secret number

while True:  # Infinite loop until the correct number is entered
    user_input = int(input("Enter the secret number: "))

    if user_input == secret_number:
        print("Congratulations! You can win a prize.")
        break  # Exit the loop when the correct number is entered
    else:
        print("Incorrect. Please try again.")


# 4. Create a while loop that will iterate over the list of names 
# and print out only the following name: William

names= ['Avery','Paige','William','Ade','Jasmyn','Crystal']

names = ['Avery', 'Paige', 'William', 'Ade', 'Jasmyn', 'Crystal']

index = 0
while index < len(names):
    if names[index] == 'William':
        print(names[index])
    index += 1



# 5. Create a loop that will ask the user to add a new string value to the list of names above.
# hint you will need use append().  

names = ['Avery', 'Paige', 'William', 'Ade', 'Jasmyn', 'Crystal']

while True:
    new_name = input("Enter a new name to add to the list (or 'q' to quit): ")
    
    if new_name.lower() == 'q':
        break  # Exit the loop if the user enters 'q'
    
    names.append(new_name)  # Add the new name to the list

print("Updated list of names:")
print(names)
 

# BONUS QUESTION


**FOR Loop:**

1. **Iteration Over a Sequence:** A for loop is used for iterating over a sequence (such as a list, tuple, string, or range) or other iterable objects. It iterates over a predefined sequence and performs an operation on each element in the sequence.

2. **Controlled Iteration:** In a for loop, the number of iterations is determined by the length of the sequence. It automatically iterates through all the items in the sequence.

3. **Simplified Syntax:** For loops have a more compact and simplified syntax. They typically consist of a header line that defines the loop, followed by an indented block of code that is executed in each iteration.

4. **Ideal for Known Iteration:** For loops are ideal when you know how many times you want to iterate, and when you have a predefined collection of items to iterate over.

**WHILE Loop:**

1. **Conditional Iteration:** A while loop is used for conditional iteration. It repeats a block of code as long as a specified condition is true. It's not limited to iterating over sequences; it can be used for a wide range of looping scenarios.

2. **Dynamic Iteration:** The number of iterations in a while loop is not fixed; it depends on the condition. This means you can have more flexibility in determining when the loop should terminate.

3. **Flexible Syntax:** While loops have a more flexible syntax as they rely on a condition to control the loop. You need to manually increment or change the loop control variable inside the loop.

4. **Ideal for Unknown Iteration:** While loops are suitable when you don't know in advance how many iterations you need, and you want to iterate based on a condition.

In summary, the key differences between for and while loops are related to the type of iteration they are best suited for and their syntax. For loops are ideal for known, sequential iteration, while while loops are more versatile and suitable for conditional, dynamic iteration. Your choice between them depends on the specific requirements of your program.

