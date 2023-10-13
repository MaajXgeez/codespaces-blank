def check_weather(temperature):
    if temperature > 75.00:
        return "It is hot outside."
    elif temperature < 70.00:
        return "It is cold outside."
    else:
        return "The weather is perfect."

# User's input (temperature as a float)
user_temperature = float(input("Enter the temperature: "))

# Call the function and print the result
weather_message = check_weather(user_temperature)
print(weather_message)