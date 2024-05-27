print("Stage 5 \n\n")


def same_by(characteristic, objects):
    if not objects:
        return True
    first = characteristic(objects[0])
    for obj in objects:
        if characteristic(obj) != first:
            return False
    return True


values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
