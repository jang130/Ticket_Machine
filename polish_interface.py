from system import choice, WrongOptionError

class PL:
    def __init__(self):
        pass

    def menu(self):
        print('Biletomat\n\r Wybierz opcje: ')
        print('1. Zakup biletu kartonikowego\n\r2. Zakup biletu okresowego')
        print('3. Sprawdzenie ważności biletu\n\r4. Sprawdzenie środków')
        print('5. Zgłoś problem\n\r6. Zakończ')
        print('>')

    def paper_ticket_type(self):
        print('Wybierz typ biletu:\n>')
        print('1. 20 minutowy\n2. 75 minutowy')
        print('3. 24 godzinny\n4. 72 godzinny\n>')


    def personal_data(self, type_of_name):
        if type_of_name == 'first':
            print('Wprowadź swoje imie:\n>')
        elif type_of_name == 'last':
            print('Wprowadź swoje nazwisko:\n>')
        else:
            raise WrongOptionError
        return


    def go_back(self):
        print('Czu chcesz wrócić do menu głównego?\n1. Tak\n2. Nie')
        if choice() == '1':
            self.options()
        elif choice() == '2':
            pass