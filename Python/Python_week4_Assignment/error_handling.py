filename = input("Enter the filename you want to read: ")

try:
    with open(filename, "r") as f:
        content = f.read()
    print("✅ File content loaded successfully:")
    print(content)

except FileNotFoundError:
    print(f"❌ The file '{filename}' was not found.")
except PermissionError:
    print(f"⚠️ You don’t have permission to read '{filename}'.")
except Exception as e:
    print(f"⚠️ An unexpected error occurred: {e}")
