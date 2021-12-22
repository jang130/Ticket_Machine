import english_interface
import polish_interface
from system import WrongOptionError, choice, paper_ticket



def choose_language():
    print('Available languages: \n1.Polish\n2.English\n>')
    option = choice()
    if option == '1':
        #polish()
        pass
    elif option == '2':
        english()
    else:
        raise WrongOptionError



def english():
    language = english_interface.EN()
    language.menu()
    options(language)
'''
def polish():
    language = polish_interface.PL()
    language.text()
'''

def options(language):
    if choice() == '1':
        language.paper_ticket_purchase()
        paper_ticket_purchase()
        language.ticket_quantity
        ticket_quantity()
    elif choice() == '2':
        pass
    elif choice() == '3':
        pass
    elif choice() == '4':
        pass
    elif choice() == '5':
        pass
    elif choice() == '6':
        pass
    else:
        raise WrongOptionError


def paper_ticket_purchase():
    if choice() == '1':
        ticket_type = '20min'
    elif choice() == '2':
        ticket_type = '75min'
    elif choice() == '3':
        ticket_type = '24h'
    elif choice() == '4':
        ticket_type = '72h'

def ticket_quantity()
    quantity = choice()
    return quantity

choose_language()

