import Languages.English_interface
import Languages.Polish_interface
import Languages.Turkish_interface
from system import machine_system
import time
from settings import get_databases, get_ticket_prices
from error_classes import MissingFileError, TimeTicketAlreadyExistsError
from error_classes import NotEnoughMoneyError, WrongOptionError
from error_classes import PersonNotFoundError, TicketDoesNotExistError


try:
    Ticket_prices = get_ticket_prices()
    Databases = get_databases()
    operation = machine_system(Databases, Ticket_prices)
    language = 0

    def ticket_machine_init():
        ticket_data = Databases[0]
        customer_data = Databases[1]
        operation.load_file(customer_data)
        operation.tickets_load(ticket_data)
        choose_language()

    def choose_language():
        global language
        language = Languages.English_interface.EN(operation)
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
        global language
        language = Languages.English_interface.EN(operation)
        language.menu()
        options()

    def polish():
        global language
        language = Languages.Polish_interface.PL(operation)
        language.menu()
        options()

    def turkish():
        global language
        language = Languages.Turkish_interface.TR(operation)
        language.menu()
        options()

    def options():
        option = operation.choice()
        if option == '1':
            operation.system_ticket(paper_ticket())
            language.operation_done()
        elif option == '2':
            operation.system_ticket(time_ticket())
            language.operation_done()
        elif option == '3':
            expiry = operation.system_check_ticket(check_ticket())
            language.check_ticket(expiry)
        elif option == '4':
            funds = operation.system_funds_check(funds_check())
            language.funds_check(funds)
        elif option == '5':
            prepaid_tickets = operation.system_prepaid_check(funds_check())
            language.prepaid_check(prepaid_tickets)
        elif option == '6':
            problem_report()
        elif option == '7':
            language.terminate()
            time.sleep(3)
            terminate()
        else:
            operation.error_log(WrongOptionError)
            raise WrongOptionError
        time.sleep(7)
        language.terminate()
        terminate()

    def paper_ticket():
        ticket_type = paper_ticket_type()
        name = personal_data()
        return (name, ticket_type)

    def paper_ticket_type():
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

    def time_ticket_type():
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

    def funds_check():
        name = personal_data()
        return name

    def personal_data():
        language.personal_data('first')
        fname = operation.choice()
        language.personal_data('last')
        lname = operation.choice()
        name = (fname, lname)
        return name

    def time_ticket():
        ticket_type = time_ticket_type()
        name = personal_data()
        return (name, ticket_type)

    def problem_report():
        language.problem_report()
        message = operation.choice()
        operation.error_log(None, message)
        language.operation_done()

    def check_ticket():
        name = personal_data()
        return name

    def terminate():
        pass

    if __name__ == "__main__":
        ticket_machine_init()

except(WrongOptionError):
    language.WrongOption()
    time.sleep(4)
    terminate()
except(MissingFileError):
    language.MissingFile()
    time.sleep(4)
    terminate()
except(TimeTicketAlreadyExistsError):
    language.TimeTicketExists()
    time.sleep(4)
    terminate()
except(NotEnoughMoneyError):
    language.NotEnoughFunds()
    time.sleep(4)
    terminate()
except(PersonNotFoundError):
    language.CustomerNotFound()
    time.sleep(4)
    terminate()
except(TicketDoesNotExistError):
    language.TicketDoesNotExist()
    time.sleep(4)
    terminate()
