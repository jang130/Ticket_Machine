from system import choice, WrongOptionError

class EN:
    def __init__(self):
        pass


    def text(self):
        print('Ticket Machine\n\r Choose an option: ')
        print('1. Paper ticket purchase\n\r2. Long term tickets purchase')
        print('3. Check ticket expiration\n\r4. Check amout of funds')
        print('5. Report problem\n\r6. Terminate')
        print('>')
        self.options()



    def options(self):
        if choice() == 1:
            self.paper_ticket_purchase()
        elif choice() == 2:
            pass
        elif choice() == 3:
            pass
        elif choice() == 4:
            pass
        elif choice() == 5:
            pass
        elif choice() == 6:
            pass
        else:
            raise WrongOptionError

    def paper_ticket_purchase(self):
        ticket_type = ''
        print('Choose type of ticket:\n>')
        print('1. 20 minutes\n2. 75 minutes\n3. 24 hours\n4. 72 hours\n>')
        if choice() == 1:
            ticket_type = '20min'
        elif choice() == 2:
            ticket_type = '75min'
        elif choice() == 3:
            ticket_type = '24h'
        elif choice() == 4:
            ticket_type = '72h'
        quantity = self.ticket_quantity()
        #wywołanie funkcji kup bilet w w systemie

    def ticket_quantity(self):
        print('Input quantity of tickets:\n>')
        quantity = choice()
        return quantity

    def go_back():
        print('Do you want to go back to option menu?\n1. yes\n2. No')