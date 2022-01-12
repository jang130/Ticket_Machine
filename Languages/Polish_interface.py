from error_classes import WrongOptionError


class PL:
    def __init__(self, operation):
        '''
        Class that prints messages in Polish.
        And sets formatted time and date variable.

        :param operation:
        :type object:
        '''
        self.operation = operation
        time = operation.time_module(False)[0]
        date = operation.time_module(False)[1]
        self.date = f'Czas: {time} Data: {date}'

    def menu(self):
        '''
        Prints main option menu.
        '''
        self.operation.clear_console()
        print(self.date)
        print('Biletomat\n\rWybierz opcje: ')
        print('1. Zakup biletu kartonikowego\n2. Zakup biletu okresowego')
        print('3. Sprawdzenie ważności biletu\n4. Sprawdzenie środków')
        print('5. Sprawdzenie biletów prepaid\n6. Zgłoś problem\n7. Zakończ')

    def paper_ticket_type(self):
        '''
        Prints chooice of paper ticket type.
        '''
        self.operation.clear_console()
        print(self.date)
        print('Wybierz typ biletu:')
        print('1. 20 minutowy\n2. 75 minutowy')
        print('3. 24 godzinny\n4. 72 godzinny')

    def time_ticket_type(self):
        '''
        Prints chooice of time ticket type.
        '''
        self.operation.clear_console()
        print(self.date)
        print('Wybierz typ biletu:')
        print('1. Miesięczny\n2. 3 Miesięczny')
        print('3. Roczny')

    def personal_data(self, type_of_name):
        '''
        Prints information about inputting
        first name and last name.
        '''
        self.operation.clear_console()
        print(self.date)
        if type_of_name == 'first':
            print('Wprowadź swoje imie:')
        elif type_of_name == 'last':
            print('Wprowadź swoje nazwisko:')
        else:
            raise WrongOptionError
        return

    def check_ticket(self, expiry):
        '''
        Prints ticket expiry date.
        '''
        self.operation.clear_console()
        print(self.date)
        print('Ważność biletu do: ')
        print(expiry)

    def operation_done(self):
        '''
        Prints information that operation
        has been done.
        '''
        self.operation.clear_console()
        print(self.date)
        print('Operacja zakończona Powodzeniem.')

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
        print('Dostępne bilety:')
        print(output)

    def funds_check(self, funds):
        '''
        Prints avialable customer funds.
        '''
        self.operation.clear_console()
        print(self.date)
        print(f'Dostępne środki:{funds[0]}.{funds[1]}zł')

    def terminate(self):
        '''
        Prints information about
        terminating sesion.
        '''
        self.operation.clear_console()
        print(self.date)
        print('Sesja została zakończona.')

    def problem_report(self):
        '''
        Prints request to describe problem.
        '''
        self.operation.clear_console()
        print(self.date)
        print('Proszę opisać problem:')

    '''
    Errors
    '''
    def WrongOption(self):
        '''
        Prints error that choosen option
        is wrong.
        '''
        self.operation.clear_console()
        print('Wybrana opcja jest niepoprawna.')

    def MissingFile(self):
        '''
        Prints error that file not found.
        '''
        self.operation.clear_console()
        print('Nie znaleziono pliku bazy danych.')

    def TimeTicketExists(self):
        '''
        Prints error that time ticket
        is already in customers data.
        '''
        self.operation.clear_console()
        print('Bilet czasowy już istnieje')

    def NotEnoughFunds(self):
        '''
        Prints error that customer have
        insufficient funds.
        '''
        self.operation.clear_console()
        print('Niewystarczające środki')

    def CustomerNotFound(self):
        '''
        Prints error that customer is
        not in the database.
        '''
        self.operation.clear_console()
        print('Nie znaleziono klienta.')

    def TicketDoesNotExist(self):
        '''
        Prints error that ticket not found.
        '''
        self.operation.clear_console()
        print('Bilet nie istnieje')
