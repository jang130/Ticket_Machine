from error_classes import WrongOptionError


class EN:
    def __init__(self, operation):
        '''
        Class that prints messages in English.
        And sets formatted time and date variable.

        :param operation:
        :type object:
        '''
        self.operation = operation
        time = operation.time_module(False)[0]
        date = operation.time_module(False)[1]
        self.date = f'Time: {time} Date: {date}'

    def menu(self):
        '''
        Prints main option menu.
        '''
        self.operation.clear_console()
        print(self.date)
        print('Ticket Machine\n\rChoose an option: ')
        print('1. Paper ticket purchase\n\r2. Long term tickets purchase')
        print('3. Check ticket expiration\n\r4. Check amount of funds')
        print('5. Check prepaid tickets\n6. Report problem\n7. Terminate')

    def paper_ticket_type(self):
        '''
        Prints chooice of paper ticket type.
        '''
        self.operation.clear_console()
        print(self.date)
        print('Choose type of ticket:')
        print('1. 20 minutes\n2. 75 minutes\n3. 24 hours\n4. 72 hours')

    def time_ticket_type(self):
        '''
        Prints chooice of time ticket type.
        '''
        self.operation.clear_console()
        print(self.date)
        print('Choose ticket type:')
        print('1. Monthly\n2. 3 Months')
        print('3. Yearly')

    def personal_data(self, type_of_name):
        '''
        Prints information about inputting
        first name and last name.
        '''
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
        '''
        Prints ticket expiry date.
        '''
        self.operation.clear_console()
        print(self.date)
        print('Ticket is valid till: ')
        print(expiry)

    def operation_done(self):
        '''
        Prints information that operation
        has been done.
        '''
        self.operation.clear_console()
        print(self.date)
        print('The operation is successful.')

    def prepaid_check(self, prepaid_tickets):
        '''
        Prints available prepaid tickets.
        '''
        self.operation.clear_console()
        print(self.date)
        output = ''
        for ticket in prepaid_tickets:
            index = prepaid_tickets.index(ticket)
            output += f'{prepaid_tickets[index]}zł\n'
        print('Available tickets:')
        print(output)

    def funds_check(self, funds):
        '''
        Prints avialable customer funds.
        '''
        self.operation.clear_console()
        print(self.date)
        print(f'Available funds: {funds[0]}.{funds[1]} zł')

    def terminate(self):
        '''
        Prints information about
        terminating sesion.
        '''
        self.operation.clear_console()
        print(self.date)
        print('Session has been terminated.')

    def problem_report(self):
        '''
        Prints request to describe problem.
        '''
        self.operation.clear_console()
        print(self.date)
        print('Please input problem description:')

    '''
    Errors
    '''
    def WrongOption(self):
        '''
        Prints error that choosen option
        is wrong.
        '''
        self.operation.clear_console()
        print('Chosen option is incorrect')

    def MissingFile(self):
        '''
        Prints error that file not found.
        '''
        self.operation.clear_console()
        print('Database file is missing')

    def TimeTicketExists(self):
        '''
        Prints error that time ticket
        is already in customers data.
        '''
        self.operation.clear_console()
        print('Time ticket already exists')

    def NotEnoughFunds(self):
        '''
        Prints error that customer have
        insufficient funds.
        '''
        self.operation.clear_console()
        print('Insufficient funds')

    def CustomerNotFound(self):
        '''
        Prints error that customer is
        not in the database.
        '''
        self.operation.clear_console()
        print('Customer not found in the database')

    def TicketDoesNotExist(self):
        '''
        Prints error that ticket not found.
        '''
        self.operation.clear_console()
        print('Ticket does not exist')
