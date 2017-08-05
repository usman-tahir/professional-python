
# Context manager for file operations
with open('./sample.txt') as input_file:
    contents = input_file.read()
    print(contents)