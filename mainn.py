#Customer and main

from Vend_1 import Vend 

price = 0

test = Vend()

def main():
    
    try:
        start = input('Enter start for starting: ').lower()
        if start == 'start':
            run(start)
        while start != 'start':
            start = input('Enter start for starting: ').lower()
        run(start)
    except ValueError:
        main()

def run(start):
    try:
        test.showItems()
        print()
        want = input('Enter what do you want: ').lower()
        if want == 'admin':
            return mainMenu()
        elif want == 'adminend':
            return main()
            
        while not choose(want):
            want = input('Enter what do you want: ').lower()
            if want == 'admin':
                return mainMenu()
        money(want)
        run(start)
    except ValueError:
        run(start)

def choose(want):
    global price
    if test._Vend__checkName(want):
        price = test._Vend__infoAboutItems(want)
        return True
    else:
        return False
        
def money(want):
    try:
        print()
        cash = float(input('Enter a money <= 100$ or |0| for exit: '))
        if cash > 100:
            print('Please, enter money <= 100$')
            money(want)
        elif cash == 0:
            run('start')
        elif cash < price:
            print('Not enough money')
            money(want)
        elif cash == price:
            test._Vend__history(want)
            test._Vend__deleteItems(want)
            print('Thank you, bye')
        else:
            change = round(cash - price, 2)
            test._Vend__history(want)
            test._Vend__deleteItems(want)
            print('Your change is:', change, '$')
            print('Thank you, bye!')

    except ValueError:
        money(want)


def mainMenu():
    try:
        print('', 'Main menu', '1. Info about items', '2. Add items', \
              '3. Change items', '4. Delete items', '5. Info about money', \
              '6. History of sell', '7. Export to Excel', '8. Exit', sep = '\n')
        choice = int(input('Enter a choice: '))
        while choice not in range(1,9):
            choice = int(input('Enter a choice: '))
        if choice == 1:
            test._Vend__infoAboutItems()
            mainMenu()
        elif choice == 2:
            test.addItems()
            mainMenu()
        elif choice == 3:
            test.changeItems()
            mainMenu()
        elif choice == 4:
            test._Vend__deleteItems()
            mainMenu()
        elif choice == 5:
            test._Vend__infoAboutMoney()
            mainMenu()
        elif choice == 6:
            test._Vend__infoHistory()
            mainMenu()
        elif choice == 7:
            test.exportHistory()
            mainMenu()
        elif choice == 8:
            main()
    except ValueError:
        mainMenu()


main()