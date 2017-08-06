
def fibonacci():
    numbers = []
    while True:
        if len(numbers) < 2:
            numbers.append(1)
        else:
            numbers.append(sum(numbers))
            numbers.pop(0)
        yield numbers[-1]
        continue

# Create a generator
g = fibonacci()
print(g)

for i in range(10):
    print(next(g))
