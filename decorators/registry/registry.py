
registry = []

def register(decorated):
    registry.append(decorated)
    return decorated

@register
def foo():
    return 3

@register
def bar():
    return 5

# Execute the functions inside the registry
answers = []
for function in registry:
    answers.append(function())

print("answers: %s" % str(answers))
