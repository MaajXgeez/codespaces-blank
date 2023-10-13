


def multiply_by_three(input_list):
    # Initialize an empty list to store the results
    result_list = []

    # Iterate through the input list and multiply each value by three
    for value in input_list:
        result_list.append(value * 3)

    return result_list

# Example list of values
input_values = [1, 2, 3, 4, 5]

# Call the function and print the result
result = multiply_by_three(input_values)
print("Original List:", input_values)
print("List after multiplying by three:", result)