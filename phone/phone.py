def func(phone):
    if phone.find("+7") != 0 and phone.find("8") != 0:
        return 'error'

    if not all(phone.split("-")):
        return 'error'
    else:
        phone = phone.replace("-", "")

    start_bt = phone.find("(")
    end_bt = phone.find(")")
    if start_bt > -1:
        if end_bt < start_bt or not phone[start_bt + 1:end_bt].isdigit() \
                or not phone.count("(") == 1 or not phone.count(")") == 1:
            return 'error'
    else:
        if end_bt > -1:
            return 'error'

    phone = phone.replace("(", "")
    phone = phone.replace(")", "")

    if phone.find("8") == 0:
        phone = "+7" + phone[1:]

    if not phone[1:].isdigit() or not len(phone[1:]) == 11:
        return 'error'

    return phone


print("Enter phone number:\n")
phone = "".join(input().split())
print(func(phone))
