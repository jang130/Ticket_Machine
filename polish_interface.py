from system import choice, WrongOptionError, time_module, clear_console

class PL:
    def __init__(self):
        self.date = f'Czas: {time_module()[0]} Data: {time_module()[1]}'

    def menu(self):
        clear_console()
        print(self.date)
        print('Biletomat\n\rWybierz opcje: ')
        print('1. Zakup biletu kartonikowego\n\r2. Zakup biletu okresowego')
        print('3. Sprawdzenie ważności biletu\n\r4. Sprawdzenie środków')
        print('5. Zgłoś problem\n\r6. Zakończ')


    def paper_ticket_type(self):
        clear_console()
        print(self.date)
        print('Wybierz typ biletu:')
        print('1. 20 minutowy\n2. 75 minutowy')
        print('3. 24 godzinny\n4. 72 godzinny')


    def personal_data(self, type_of_name):
        clear_console()
        print(self.date)
        if type_of_name == 'first':
            print('Wprowadź swoje imie:')
        elif type_of_name == 'last':
            print('Wprowadź swoje nazwisko:')
        else:
            raise WrongOptionError
        return


    def go_back(self):
        clear_console()
        print(self.date)
        print('Czu chcesz wrócić do menu głównego?\n1. Tak\n2. Nie')
        if choice() == '1':
            self.options()
        elif choice() == '2':
            pass