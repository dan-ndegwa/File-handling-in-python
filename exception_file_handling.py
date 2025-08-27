## File Read & Write Challenge
# Create a program that reads a file and writes a modified version to a new file.

old_file = open("File", "w")
old_file.write(f"Output of old_file: This is the old version of data \n")
old_file.close()

entry_data = open("File", "a")
new_file = entry_data.write(f"Output of entry_data: This is the updated version of the inputted file")
entry_data.close()

with open("File", "r") as file:
    content = file.read()
    print(content)


## Error Handling Lab Assignment
#Question:  Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.

# Here is my mini program promting user for a file name, which then my program runs to check and handles errors incase the file is missing

user_input = input("File Name: ")
try:
    with open((user_input), "r") as file:
        content = file.read()

except FileNotFoundError:
    print("File Not Found. Try Again!")





