my_list = [1, 2, 3, 4, 5]
length = len(my_list)
print("Length of the list:", length)

number = 42
number_str = str(number)
print("Converted to string:", number_str)

numbers = [10, 45, 3, 28, 51, 7]
largest = max(numbers)
smallest = min(numbers)
print("Largest number:", largest)
print("Smallest number:", smallest)



num1 = 10
num2 = 20

if num1 == num2:
    print("The numbers are equal.")
else:
    print("The numbers are not equal.")

    score = 85
result = ""

if score >= 90:
    result = "A"
elif score >= 80:
    result = "B"
else:
    result = "C"

print("Your grade is:", result)

number = 12

if number > 0 and number % 2 == 0:
    print("The number is a positive even number.")
else:
    print("The number does not meet the criteria.")

    def multiply_by_three(numbers):
    result = []
    for num in numbers:
        multiplied = num * 3
        result.append(multiplied)
    return result
  
# List of numbers
li\
    st_of_numbers = [100, 20, 34, 45, 75, 9, 60]

# Call the function and print the result
result_list = multiply_by_three(list_of_numbers)
print("Original list:", list_of_numbers)
print("List after multiplying by 3:", result_list)

def is_palindrome(word):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    cleaned_word = word.replace(" ", "").lower()
    
    # Reverse the cleaned word
    reversed_word = cleaned_word[::-1]
    
    # Check if the original word is the same as the reversed word
    return cleaned_word == reversed_word

# User's input
user_input = input("Enter a word: ")

# Call the function and check if it's a palindrome
if is_palindrome(user_input):
    print(f"{user_input} is a palindrome.")
else:
    print(f"{user_input} is not a palindrome.")

