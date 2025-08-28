# File Read, Modify, Write with Error Handling

def process_file():
    # Ask user for the filename to read
    input_file = input("Enter the name of the file you want to read: ")
    output_file = "output.txt"  # The new file to be created

    try:
        # Open and read the input file
        with open(input_file, "r") as f:
            content = f.read()

        # Modify the content ( changing it to uppercase)
        modified_content = content.upper()

        # Write the modified content into a new file
        with open(output_file, "w") as f:
            f.write(modified_content)

        print(f"Success! Modified content written to '{output_file}'")

    # Handling possible errors
    except FileNotFoundError:
        print(f"The file '{input_file}' was not found. Please check the name and try again.")
    except PermissionError:
        print(f"You don’t have permission to read '{input_file}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Run the program
process_file()
