# file_handling_assignment.py

def create_and_write_file():
    try:
        # Creating a new file and writing to it
        with open("my_file.txt", "w") as file:
            file.write("Hello, world!\n")
            file.write("Python file handling tutorial.\n")
            file.write("This file contains both text and numbers: 12345\n")
        print("File 'my_file.txt' created and initial content written.")
    except PermissionError:
        print("Permission denied: Unable to write to the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def read_and_display_file():
    try:
        # Reading and displaying the content of the file
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("\nFile Content:")
            print(content)
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def append_to_file():
    try:
        # Appending additional lines to the file
        with open("my_file.txt", "a") as file:
            file.write("Appending more content...\n")
            file.write("Python makes file handling easy.\n")
            file.write("Numbers can also be written: 67890\n")
        print("New content appended to 'my_file.txt'.")
    except PermissionError:
        print("Permission denied: Unable to append to the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    try:
        # Step 1: Create and write initial content to the file
        create_and_write_file()
        
        # Step 2: Read and display the content of the file
        read_and_display_file()
        
        # Step 3: Append new lines to the file
        append_to_file()
        
        # Step 4: Read and display the updated content of the file
        read_and_display_file()
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("\nFile operations completed.")

if __name__ == "__main__":
    main()

