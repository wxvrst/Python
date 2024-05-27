print("Stage 2 \n\n")


def simple_map(transformation, values):
    result = []
    for elem in values:
        result.append(transformation(elem))
    return result


values = [1, 3, 1, 5, 7]
operation = lambda x: x + 5
print(*simple_map(operation, values))
