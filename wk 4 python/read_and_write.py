filename = input("Enter the filename to read: ")

# Check if the user has entered a valid filename (not empty)
if not filename:
    print("Error: You must enter a valid filename.")
else:
    # Optional: Check if the filename ends with ".txt"
    if not filename.endswith(".txt"):
        print("Error: Please provide a valid text file (.txt).")
    else:
        try:
            # Try to open and read the file
            with open(filename, "r") as file:
                content = file.read()  # Read the entire content

            # Modify the content (convert to uppercase)
            modified_content = content.upper()

            # Write the modified content to a new file
            with open("output.txt", "w") as new_file:
                new_file.write(modified_content)  # Write the content to the new file

            print("File has been modified and saved to 'output.txt'.")

        except FileNotFoundError:
            print(f"Error: The file {filename} does not exist.")
        
        except IOError:
            print(f"Error: Could not read or write to the file {filename}.")
