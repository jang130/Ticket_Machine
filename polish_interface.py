from system import WrongOptionError, machine_system

class PL:
    def __init__(self, operation):
        self.operation = operation
        self.date = f'Czas: {operation.time_module()[0]} Data: {operation.time_module()[1]}'

    def menu(self):
        self.operation.clear_console()
        print(self.date)
        print('Biletomat\n\rWybierz opcje: ')
        print('1. Zakup biletu kartonikowego\n\r2. Zakup biletu okresowego')
        print('3. Sprawdzenie ważności biletu\n\r4. Sprawdzenie środków')
        print('5. Zgłoś problem\n\r6. Zakończ')


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

    def go_back(self):
        self.operation.clear_console()
        print(self.date)
        print('Czu chcesz wrócić do menu głównego?\n1. Tak\n2. Nie')
        if self.operation.choice() == '1':
            self.options()
        elif self.operation.choice() == '2':
            pass