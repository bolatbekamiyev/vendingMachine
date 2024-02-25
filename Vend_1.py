from datetime import datetime                       #For timestamp
import xlsxwriter                                   #Exports data to Excel file


class Vend: 
    
    count = 1                                       #For id of sold items in history
    
    def __init__(self):
        self.__items = {'naked' : {'price' : 2.79, 'amount' : 5},    #dict
                        'aquafina' : {'price' : 2.20, 'amount' : 5}, 
                        'coffee' : {'price' : 4.59, 'amount' : 6}}
        
        self.__money = {'amount' : 100}                              #dict
        self.history = []                                            #list of tuple
        self.names = {'naked', 'aquafina', 'coffee'}                 #set
        
    def __repr__(self):
        return 'The object Vend created by Bolatbek Amiyev'
    
    
    
    #Adds items to the dictionary |__items|
    def addItems(self):   
        if len(self.__items) < 20:
            name = input('Enter a name of item: ').lower()
            if not self.__checkName(name):
                price = float(input('Enter a price: '))
                amount = int(input('Enter the amount of the item: '))
                self.__items[name] = {'price' : price, 'amount' : amount}
                self.names.add(name)
                if self.askContinue():
                    self.addItems()
            else:
                print('This item is already there')
                self.addItems()
        else:
            print('No empty sections')
    
    
    #This method asks if you want to continue or no
    def askContinue(self):  
        
        answer = input('Do you want to continue (yes or no)? ').lower()
        if answer[0] == 'y':
            return True
        elif answer[0] == 'n':
            print('Thank you!')
        else:
            print('The answer is unclear please write yes or no')
            self.askContinue()
    
    
    #Removes items from the dictionary |__items|
    def __deleteItems(self, item = 0): 
        
        if item == 0:
            item = input('Enter the name of the item or exit: ').lower()
            if item == 'exit':
                print('Thank you!')
                return None
            while not self.__checkName(item):
                print('There is no such item!')
                item = input('Enter the correct name or exit: ').lower()
                if item == 'exit':
                    print('Thank you!')
                    return None
            self.__checkName(item)
            self.__items.pop(item)
            self.names.discard(item)
            print('Done')
           
               
        elif self.__checkName(item):
            self.__items[item]['amount'] -= 1
            if self.__items[item]['amount'] == 0:
                self.__items.pop(item)
                self.names.discard(item)
        else:
            print('Error')
    
    
    #Checks if an items is in the set |name|
    def __checkName(self, name): 
        if name in self.names:
            return True
        else:
            return False
        
    def __add__(self, value):
        if isinstance(value, (int, float)):
            return self.__money['amount'] + value
    

    #Helps to change the information about the subject        
    def changeItems(self): 
        
        value = input('What do you want to change (name|price|amount) or enter exit? ').lower()
        
        if value == 'exit':
            print('Thank you!')
            return None
        
        elif value == 'name':
            old_key = input('Enter the old name or exit: ').lower()
            if old_key == 'exit':
                print('Thank you!')
                return None
            while not self.__checkName(old_key):
                print('There is no such item!')
                old_key = input('Enter the correct name or exit: ').lower()
                if old_key == 'exit':
                    print('Thank you!')
                    return None
            new_key = input('Enter a new name: ').lower()
            self.__items[new_key] = self.__items.pop(old_key)
            self.names.discard(old_key)
            self.names.add(new_key)
            if self.askContinue():
                    self.changeItems()
        
        elif value == 'price':
            name = input('Enter a name of item or exit: ')
            if name == 'exit':
                print('Thank you!')
                return None
            while not self.__checkName(name):
                print('There is no such item!')
                name = input('Enter the correct name or exit: ').lower()
                if name == 'exit':
                    print('Thank you')
                    return None
            new_price = float(input('Enter a new price: '))
            self.__items[name]['price'] = new_price
            print('All set!')
            if self.askContinue():
                    self.changeItems()
                    
        elif value == 'amount':
            name = input('Enter a name of item or exit: ')
            if name == 'exit':
                print('Thank you!')
                return None
            while not self.__checkName(name):
                print('There is no such item!')
                name = input('Enter the correct name or exit: ').lower()
                if name == 'exit':
                    print('Thank you')
                    return None
            new_amount = int(input('Enter a new amount of the product: '))
            self.__items[name]['amount'] = new_amount
            print('All set!')
            if self.askContinue():
                    self.changeItems()
                    
        else:
            value = input('There is no such item, enter |yes| to start over or |exit| to exit: ').lower()
            if value[0] == 'y':
                self.changeItems()
            else:
                print('Thank you!')
                
    
    
    #Provides information about items
    def __infoAboutItems(self, value = 0, admin = 0): 
        if value == 0:
            value = input('Enter |the exact name| for a specific item or |all| for the entire list: ').lower()
            admin = input('Enter password: ')
            if value == 'all' and admin == 'admin':
                for i in self.__items:
                    print(i.capitalize(), '|', 'price -', self.__items[i]['price'], '| amount -', self.__items[i]['amount'])
                if self.askContinue():
                    self.__infoAboutItems()
            elif self.__checkName(value) and admin == 'admin':
                print(value.capitalize(), '|', 'price -', self.__items[value]['price'], '| amount -', self.__items[value]['amount'])
                if self.askContinue():
                        self.__infoAboutItems()
            else:
                value = input('There is no such item, enter |yes| to start over or |exit| to exit: ').lower()
                if value[0] == 'y':
                    self.__infoAboutItems()
                else:
                    print('Thank you!')
            
        elif self.__checkName(value): 
            if admin == 0:
                print(value.capitalize(), '|', 'price -', self.__items[value]['price'])
                return self.__items[value]['price']
            else:
                print('Error')
        else:
            print('There is no such item')
    
    
    #Provides information about money
    def __infoAboutMoney(self): 
        print()
        print('amount -', self.__money['amount'], '$')
    
    
    #Provides historical sales information
    def __infoHistory(self):    
        print()
        for i in range(len(self.history)):
            print(self.history[i][0], '|', self.history[i][1][0], '|', self.history[i][1][1])
    

    #Shows available items for the customer
    def showItems(self):  
        print(' ', '---------- Available Items -----------', ' ', sep = '\n')
        for i in self.__items:
            print(i.capitalize(), '|'.rjust(12 - len(i)), 'price -', self.__items[i]['price'])


    #Saves the history of the sale
    def __history(self, item): 
        current_time = datetime.now().strftime('%H:%M:%S %m/%d/%Y')
        log = (Vend.count, (item, current_time, self.__items[item]['price']))
        self.history.append(log)
        self.__money['amount'] += self.__items[item]['price']
        Vend.count += 1
    
    
    #Exports data to Excel file
    def exportHistory(self):  
    
        current_time = datetime.now().strftime('%H-%M-%S_%m-%d-%Y')
        data = xlsxwriter.Workbook(current_time + '.xlsx')
        datasheet1 = data.add_worksheet("History of selling")
        datasheet2 = data.add_worksheet("Available items")
        bold = data.add_format({'bold': True})
        money_format = data.add_format({'num_format': '$#,##0.##'})
        bold_money = data.add_format({'bold': True, 'num_format': '$#,##0.00'})
        row = 0
        column = 0
        datasheet1.write(row, column, 'id', bold)
        datasheet1.write(row, column + 1, 'name', bold)
        datasheet1.write(row, column + 2, 'datetime', bold)
        datasheet1.write(row, column + 3, 'recent_price', bold)
        datasheet2.write(row, column, 'id', bold)
        datasheet2.write(row, column + 1, 'name', bold)
        datasheet2.write(row, column + 2, 'price', bold)
        datasheet2.write(row, column + 3, 'amount', bold)
        row = 1
        id = 1
        for i in self.history:
            datasheet1.write(row, column, i[0])
            datasheet1.write(row, column + 1, i[1][0].capitalize())
            datasheet1.write(row, column + 2, i[1][1])
            datasheet1.write(row, column + 3, i[1][2], money_format)
            row += 1
        total = '(D2:' + 'D' + str(row) +')'
        datasheet1.write(row, column + 3, '=SUM' + total, bold_money)
        row = 1
        for i in self.__items:
            datasheet2.write(row, column, id)
            datasheet2.write(row, column + 1, i.capitalize())
            datasheet2.write(row, column + 2, self.__items[i]['price'], money_format)
            datasheet2.write(row, column + 3, self.__items[i]['amount'])
            id += 1
            row += 1
        data.close()
        print(' ', 'Successfully exported', sep = '\n')