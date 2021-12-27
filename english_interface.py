from datetime import time
from system import WrongOptionError, machine_system




class EN:
    def __init__(self, operation):
        self.operation = operation
        self.date = f'Time: {operation.time_module()[0]} Date: {operation.time_module()[1]}'



    def menu(self):
        self.operation.clear_console()
        print(self.date)
        print('Ticket Machine\n\rChoose an option: ')
        print('1. Paper ticket purchase\n\r2. Long term tickets purchase')
        print('3. Check ticket expiration\n\r4. Check amout of funds')
        print('5. Report problem\n\r6. Terminate')


    def paper_ticket_type(self):
        self.operation.clear_console()
        print(self.date)
        print('Choose type of ticket:')
        print('1. 20 minutes\n2. 75 minutes\n3. 24 hours\n4. 72 hours')


    def personal_data(self, type_of_name):
        self.operation.clear_console()
        print(self.date)
        if type_of_name == 'first':
            print('Input your first name:')
        elif type_of_name == 'last':
            print('Input your last name:')
        else:
            raise WrongOptionError
        return


    def go_back(self):
        self.operation.clear_console()
        print(self.date)
        print('Do you want to go back to option menu?\n1. yes\n2. No')
        if self.operation.choice() == '1':
            self.options()
        elif self.operation.choice() == '2':
            pass