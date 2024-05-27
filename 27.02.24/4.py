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
