from error_classes import WrongOptionError
class PL:
    def __init__(self, operation):
        self.operation = operation
        time = operation.time_module(False)[0]
        date = operation.time_module(False)[1]
        self.date = f'Czas: {time} Data: {date}'

    def menu(self):
        self.operation.clear_console()
        print(self.date)
        print('Biletomat\n\rWybierz opcje: ')
        print('1. Zakup biletu kartonikowego\n2. Zakup biletu okresowego')
        print('3. Sprawdzenie ważności biletu\n4. Sprawdzenie środków')
        print('5. Sprawdzenie biletów prepaid\n6. Zgłoś problem\n7. Zakończ')

    def paper_ticket_type(self):
        self.operation.clear_console()
        print(self.date)
        print('Wybierz typ biletu:')
        print('1. 20 minutowy\n2. 75 minutowy')
        print('3. 24 godzinny\n4. 72 godzinny')

    def time_ticket_type(self):
        self.operation.clear_console()
        print(self.date)
        print('Wybierz typ biletu:')
        print('1. Miesięczny\n2. 3 Miesięczny')
        print('3. Roczny')

    def personal_data(self, type_of_name):
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
        self.operation.clear_console()
        print(self.date)
        print('Ważność biletu do: ')
        print(expiry)

    def operation_done(self):
        self.operation.clear_console()
        print(self.date)
        print('Operacja zakończona Powodzeniem.')

    def prepaid_check(self, prepaid_tickets):
        self.operation.clear_console()
        print(self.date)
        output = ''
        for ticket in prepaid_tickets:
            index = prepaid_tickets.index(ticket)
            output += f'{prepaid_tickets[index]}zł\n'
        print('Dostępne bilety:')
        print(output)

    def funds_check(self, funds):
        self.operation.clear_console()
        print(self.date)
        print(f'Dostępne środki:{funds[0]}.{funds[1]}zł')

    def terminate(self):
        self.operation.clear_console()
        print(self.date)
        print('Sesja została zakończona.')

    def problem_report(self):
        self.operation.clear_console()
        print(self.date)
        print('Proszę opisać problem:')
