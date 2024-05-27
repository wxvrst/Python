class PasswordExeption(Exception):
    pass
class LengthError(PasswordExeption):
    pass
class LetterError(PasswordExeption):
    pass
class DigitError(PasswordExeption):
    pass
class SequenceError(PasswordExeption):
    pass
def check_password(password):
    print(password)
    if len(password)<9:
        print("BAD: password is too short")

    if not any(map(str.isalpha,password)):
        print("BAD: no alpha")
        return 0
    if not any(map(str.isdigit,password)):
        print("BAD: no digit")
        return 0
    if not any(map(str.islower,password)):
        print("BAD: no lower")
        return 0
    if not any(map(str.isupper,password)):
        print("BAD: no upper")
        return 0

    for i in range(len(password)-2):
        if ord(password[i])==ord(password[i+1])-1==ord(password[i+2])-2:
            print("BAD: include bad combinations")
            return 0
    
    print("OK")
    return 1


    

password="".join(input().split())
check_password(password)