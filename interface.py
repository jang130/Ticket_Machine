from datetime import date, time
from os import name
import english_interface
import polish_interface
import system
from system import WrongOptionError, machine_system

operation = machine_system()
operation.load_file('Customer_data')
def choose_language():
    operation.clear_console()
    print('Available languages: \n1.Polish\n2.English')
    option = operation.choice()
    if option == '1':
        polish()
    elif option == '2':
        english()
    else:
        raise WrongOptionError



def english():
    language = english_interface.EN(operation)
    language.menu()
    options(language)

def polish():
    language = polish_interface.PL(operation)
    language.menu()
    options(language)


def options(language):
    option = operation.choice()
    if option == '1':
        operation.system_ticket(paper_ticket(language))
    elif option == '2':
        operation.system_ticket(time_ticket(language))
    elif option == '3':
        operation.system_check_ticket(check_ticket(language))
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
    name = personal_data(language)
    return (name, ticket_type)

def paper_ticket_type(language):
    language.paper_ticket_type()
    option = operation.choice()
    if option == '1':
        ticket_type = '20min'
    elif option == '2':
        ticket_type = '75min'
    elif option == '3':
        ticket_type = '24h'
    elif option == '4':
        ticket_type = '72h'
    else:
        raise WrongOptionError
    return ticket_type

def time_ticket_type(language):
    language.time_ticket_type()
    option = operation.choice()
    if option == '1':
        ticket_type = '1m'
    elif option == '2':
        ticket_type = '3m'
    elif option == '3':
        ticket_type = '1y'
    else:
        raise WrongOptionError
    return ticket_type


def personal_data(language):
    language.personal_data('first')
    fname = operation.choice()
    language.personal_data('last')
    lname = operation.choice()
    name = (fname, lname)
    return name

def time_ticket(language):
    ticket_type = time_ticket_type(language)
    name = personal_data(language)
    return (name, ticket_type)

def check_ticket(language):
    name = personal_data(language)
    return name

def send_to_system(input):
    return input
choose_language()

