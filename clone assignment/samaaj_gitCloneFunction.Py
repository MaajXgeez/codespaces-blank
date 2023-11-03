import os

def create_folder_and_calculate_sum(folder_name, numbers):
    # Create a new folder
    try:
        os.mkdir(folder_name)
        print(f"Folder '{folder_name}' created successfully.")
    except FileExistsError:
        print(f"Folder '{folder_name}' already exists.")

    # Calculate the sum of numbers
    total = sum(numbers)
    print(f"The sum of the numbers in the list is: {total}")

# Example usage
folder_name = "cloneAssignment"
number_list = [1, 2, 3, 4, 5]
create_folder_and_calculate_sum(folder_name, number_list)
