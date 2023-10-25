# 1. In your own words, describe what a for loop is?

A for loop is a fundamental programming construct that allows you to repeat a specific block of code a certain number of times or for each element in a collection (such as a list, array, or range of values). It provides a structured way to automate repetitive tasks and iterate through data without the need to write the same code multiple times.

In a for loop, you typically define a control variable (often called an iterator or index) that keeps track of the current iteration, set the initial value of this variable, specify a condition that determines when the loop should continue, and define how the control variable is updated after each iteration. The loop will continue executing the specified code block as long as the condition holds true, and it stops when the condition becomes false.

For example, if you want to print the numbers from 1 to 5, you can use a for loop like this in Python:

```python
for i in range(1, 6):
    print(i)




In this code, `i` is the control variable that takes on values from 1 to 5 (inclusive), and the `print` statement is executed during each iteration of the loop. This loop simplifies the process of performing the same action for multiple values or elements, making your code more efficient and concise.



# 2. What is the difference between a FOR loop and a WHILE loop?
# Provide two (2) examples of each. 

A for loop is used to iterate a specific number of times or over a collection, and it's controlled by a counter or an iterator variable.

# 3. Create a FOR loop that will go through a list of names 
# and print all the names that start with the letter "R".

names=['Michael','Rebecca','William','Kareem','Robert','Rose','Jason']

names = ['Michael', 'Rebecca', 'William', 'Kareem', 'Robert', 'Rose', 'Jason']

for name in names:
    if name.startswith('R'):
        print(name)

