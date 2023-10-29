my_variable = 42
my_string = "The value of my_variable is: "

# Concatenate the string and variable
result = my_string + str(my_variable)

# Specify the file path
file_path = "oput.txt"

# Open the file in write mode
with open(file_path, "w") as file:
    # Write the concatenated string to the file
    file.write(result)