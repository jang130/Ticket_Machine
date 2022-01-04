import Languages.English_interface
import Languages.Polish_interface
import Languages.Turkish_interface
from system import WrongOptionError, machine_system
import time

operation = machine_system()

def choose_language():
    operation.load_file('Customer_data')
    operation.tickets_load('Ticket_data')
    operation.clear_console()
    print('Available languages: \n1.Polish\n2.English\n3.Turkish')
    option = operation.choice()
    if option == '1':
        polish()
    elif option == '2':
        english()
    elif option == '3':
        turkish()
    else:
        operation.error_log(WrongOptionError)
        raise WrongOptionError


def english():
    language = Languages.English_interface.EN(operation)
    language.menu()
    options(language)


def polish():
    language = Languages.Polish_interface.PL(operation)
    language.menu()
    options(language)


def turkish():
    language = Languages.Turkish_interface.TR(operation)
    language.menu()
    options(language)


def options(language):
    option = operation.choice()
    if option == '1':
        state = 1
        operation.system_ticket(paper_ticket(language))
        language.operation_done()
    elif option == '2':
        state = 2
        operation.system_ticket(time_ticket(language))
        language.operation_done()
    elif option == '3':
        state = 3
        expiry = operation.system_check_ticket(check_ticket(language))
        language.check_ticket(expiry)
    elif option == '4':
        state = 4
        funds = operation.system_funds_check(funds_check(language))
        language.funds_check(funds)
    elif option == '5':
        state = 5
        prepaid_tickets = operation.system_prepaid_check(funds_check(language))
        language.prepaid_check(prepaid_tickets)
    elif option == '6':
        state = 6
        problem_report(language, state)
    elif option == '7':
        state = 7
        language.terminate()
        time.sleep(3)
        terminate()
    else:
        operation.error_log(WrongOptionError)
        raise WrongOptionError
    time.sleep(7)
    language.terminate()
    terminate()

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
        operation.error_log(WrongOptionError)
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
        operation.error_log(WrongOptionError)
        raise WrongOptionError
    return ticket_type

def funds_check(language):
    name = personal_data(language)
    return name


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


def problem_report(language, state):
    language.problem_report()
    message = operation.choice()
    operation.error_log(None, message)
    language.operation_done()


def check_ticket(language):
    name = personal_data(language)
    return name


def terminate():
    choose_language()

choose_language()

