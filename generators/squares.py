
def squares(cursor = 1):
    cursor = 1
    while True:
        response = yield cursor ** 2
        if response:
            cursor = int(response)
        else:
            cursor += 1

# Print out squares up to 10
s = squares()
print(next(s))
print(next(s))
print(s.send(7))
print(next(s))
