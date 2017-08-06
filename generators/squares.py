
def squares():
    cursor = 1
    while True:
        yield cursor ** 2
        cursor += 1

# Print out squares up to 10
s = squares()
for i in range(1, 11):
    print(next(s))
