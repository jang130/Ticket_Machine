from system import choice, WrongOptionError

class EN:
    def __init__(self):
        pass


    def menu(self):
        print('Ticket Machine\n\r Choose an option: ')
        print('1. Paper ticket purchase\n\r2. Long term tickets purchase')
        print('3. Check ticket expiration\n\r4. Check amout of funds')
        print('5. Report problem\n\r6. Terminate')
        print('>')

    def paper_ticket_purchase(self):
        ticket_type = ''
        print('Choose type of ticket:\n>')
        print('1. 20 minutes\n2. 75 minutes\n3. 24 hours\n4. 72 hours\n>')
        quantity = self.ticket_quantity()
        name = self.personal_data()
        print(name, quantity, ticket_type)
        #wywołanie funkcji kup bilet w w systemie


    def ticket_quantity(self):
        print('Input quantity of tickets:\n>')


    def personal_data(self):
        print('Input your first name:\n>')
        fname = choice()
        print('Input your last name:\n>')
        lname = choice()
        name = (fname, lname)
        return name

    def go_back(self):
        print('Do you want to go back to option menu?\n1. yes\n2. No')
        if choice() == '1':
            self.options()
        elif choice() == '2':
            pass