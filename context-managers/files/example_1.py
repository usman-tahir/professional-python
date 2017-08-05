
# Basic example for opening/closing a file
try:
    f = open('./sample.txt', 'r')
    contents = f.read()
    print(contents)
finally:
    f.close()