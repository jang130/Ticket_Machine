from datetime import time
from system import WrongOptionError, machine_system




class EN:
    def __init__(self, operation):
        self.operation = operation
        self.date = f'Time: {operation.time_module(False)[0]} Date: {operation.time_module(False)[1]}'



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

    def time_ticket_type(self):
        self.operation.clear_console()
        print(self.date)
        print('Wybierz typ biletu:')
        print('1. Monthly\n2. 3 Months')
        print('3. Yearly')

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

    def check_ticket(self, expiry):
        self.operation.clear_console()
        print(self.date)
        print('Ticket is valid till: ')
        print(expiry)

    def operation_done(self):
        self.operation.clear_console()
        print(self.date)
        print('The operation is successful.')

    def prepaid_check(self, funds):
        self.operation.clear_console()
        print(self.date)
        print(f'Available funds: {funds[0]}.{funds[1]} zł')

    def go_back(self):
        self.operation.clear_console()
        print(self.date)
        print('Do you want to go back to option menu?\n1. yes\n2. No')

    def terminate(self):
        self.operation.clear_console()
        print(self.date)
        print('Session has been terminated.')