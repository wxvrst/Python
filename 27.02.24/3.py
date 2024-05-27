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
