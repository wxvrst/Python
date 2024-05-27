##############
# 1
##############
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

##############
# 2
##############
print("Stage 2 \n\n")


def simple_map(transformation, values):
    result = []
    for elem in values:
        result.append(transformation(elem))
    return result


values = [1, 3, 1, 5, 7]
operation = lambda x: x + 5
print(*simple_map(operation, values))

##############
# 3
##############
print("Stage 3 \n\n")

one = 5
two = 4
three = 0
roman_numbers = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
                 'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
                 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}


def to_roman(number):
    roman = ''
    for letter, value in roman_numbers.items():
        while number >= value:
            roman += letter
            number -= value
    return roman


def roman():
    global three
    three = one + two
    print(f"{to_roman(one)}+{to_roman(two)}={to_roman(three)}")


roman()

##############
# 4
##############
print("Stage 4 \n\n")
count = []
name = []
money = []

t = 0


def get_transaction(transaction):
    if transaction == 'print_it':
        names = list(set(name))
        cash = [0,0]
        count=[0,0]
        for i, j in zip(name, money):
            if i in names:
                cash[names.index(i)]+= int(j)
                count[names.index(i)]+=1
            else:
                cash.append(j)

        print(count)
        print(name)
        print(money)
        print("\n")
        print(names)
        print(cash)
        print(count)
        return 0
    name.append(transaction[transaction.index("-") + 1: transaction.index(":")])
    money.append(transaction[transaction.index(":") + 1:])


get_transaction('8321-перевод:100')
get_transaction('214321-перевод:1000')
get_transaction('44441-оплата:10000')
get_transaction('2145-перевод:50000000')
get_transaction('print_it')

##############
# 5
##############
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
