def evaluate_data_type(user_input):
    data_type = type(user_input).__name__ # Get the data type name as a string
    
    if data_type == "int":
        return "You entered an integer."
    elif data_type == "float":
        return "You entered a float."
    elif data_type == "str":
        return "You entered a string."
    elif data_type == "bool":
        return "You entered a boolean."
    elif data_type == "list":
        return "You entered a list."
    elif data_type == "tuple":
        return "You entered a tuple."
    elif data_type == "dict":
        return "You entered a dictionary."
    else:
        return "You entered an unknown data type."

# User's input
user_input = input("Enter a value: ")

# Call the function and print the result
result_message = evaluate_data_type(user_input)
print(result_message) 
