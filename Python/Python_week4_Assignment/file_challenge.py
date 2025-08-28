def modify_file(input_file, output_file):
    try:
        with open(input_file, "r") as f:
            content = f.read()

        # Modify the content (example: make uppercase)
        modified_content = content.upper()

        with open(output_file, "w") as f:
            f.write(modified_content)

        print(f"File has been read from '{input_file}' and written to '{output_file}' successfully.")

    except FileNotFoundError:
        print(f"The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Run the function
modify_file("input.txt", "output.txt")
