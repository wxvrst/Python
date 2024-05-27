print("Stage 1 \n\n")


def arithmetic_operation(operation):
    return lambda a, b: eval("a" + operation + "b")


operation = arithmetic_operation("+")
print(operation(1, 4))
operation = arithmetic_operation("-")
print(operation(1, 4))
operation = arithmetic_operation("*")
print(operation(1, 4))
operation = arithmetic_operation("/")
print(operation(1, 4))
