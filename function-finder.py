import re

def extract_function_names(go_file_path):
    pattern = re.compile(r'\bfunc\s+(\w+)\s*\([^)]*\)')
    function_names = []

    try:
        with open(go_file_path, 'r') as file:
            for line in file:
                match = pattern.search(line)
                if match:
                    function_names.append(match.group(0))

        with open('function_names.txt', 'w') as output_file:
            for name in function_names:
                output_file.write(name + '\n')

        for name in function_names:
            print(name)
    except FileNotFoundError:
        print(f"The file at {go_file_path} was not found. Please check the path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Prompt the user for the file path
file_path = input("Enter the path to the file: ")
extract_function_names(file_path)

