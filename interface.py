import english_interface
import polish_interface
from system import WrongOptionError, choice



def choose_language():
    print('Available languages: \n1.Polish\n2.English\n>')
    option = choice()
    if option == '1':
        polish()
    elif option == '2':
        english()
    else:
        raise WrongOptionError



def english():
    language = english_interface.EN()
    language.menu()
    options(language)

def polish():
    language = polish_interface.PL()
    language.menu()
    options(language)


def options(language):
    option = choice()
    if option == '1':
        paper_ticket(language)
    elif option == '2':
        pass
    elif option == '3':
        pass
    elif option == '4':
        pass
    elif option == '5':
        pass
    elif option == '6':
        pass
    else:
        raise WrongOptionError

def paper_ticket(language):
    ticket_type = paper_ticket_type(language)
    quantity = ticket_quantity(language)
    name = personal_data(language)


def paper_ticket_type(language):
    language.paper_ticket_type()
    option = choice()
    if option == '1':
        ticket_type = '20min'
    elif option == '2':
        ticket_type = '75min'
    elif option == '3':
        ticket_type = '24h'
    elif option == '4':
        ticket_type = '72h'
    return ticket_type

def ticket_quantity(language):
    language.ticket_quantity()
    quantity = choice()
    return quantity

def personal_data(language):
    language.personal_data('first')
    fname = choice()
    language.personal_data('last')
    lname = choice()
    name = (fname, lname)
    return name

choose_language()

