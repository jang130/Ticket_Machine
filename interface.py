import Languages.English_interface
import Languages.Polish_interface
import Languages.Turkish_interface
from system import machine_system
import time
from settings import get_databases, get_ticket_prices
from error_classes import MissingFileError, TimeTicketAlreadyExistsError
from error_classes import NotEnoughMoneyError, WrongOptionError
from error_classes import PersonNotFoundError, TicketDoesNotExistError


class main_interface:
    def __init__(self) -> None:
        pass

    def ticket_machine_init(self):
        '''
        Function loads databases files and goes to
        choosing language function.
        '''
        ticket_data = Databases[0]
        customer_data = Databases[1]
        operation.load_file(customer_data)
        operation.tickets_load(ticket_data)
        self.choose_language()

    def choose_language(self):
        '''
        Function creates base language object (for errors exceptions)
        and reads choice of choosen language.
        '''

        self.language = Languages.English_interface.EN(operation)
        operation.clear_console()
        print('Available languages: \n1.Polish\n2.English\n3.Turkish')
        option = operation.choice()
        if option == '1':
            self.polish()
        elif option == '2':
            self.english()
        elif option == '3':
            self.turkish()
        else:
            operation.error_log(WrongOptionError)
            raise WrongOptionError

    def english(self):
        '''
        Creates English language object and goes to
        option menu.
        '''

        self.language = Languages.English_interface.EN(operation)
        self.language.menu()
        self.options()

    def polish(self):
        '''
        Creates Polish language object and goes to
        option menu.
        '''

        self.language = Languages.Polish_interface.PL(operation)
        self.language.menu()
        self.options()

    def turkish(self):
        '''
        Creates Turkish language object and goes to
        option menu.
        '''
        self.language = Languages.Turkish_interface.TR(operation)
        self.language.menu()
        self.options()

    def options(self):
        '''
        Function is the main option menu that chooses
        what option in which language to print and
        what operation to do.
        '''
        option = operation.choice()
        if option == '1':
            operation.system_ticket(self.paper_ticket())
            self.language.operation_done()
        elif option == '2':
            operation.system_ticket(self.time_ticket())
            self.language.operation_done()
        elif option == '3':
            expiry = operation.system_check_ticket(self.check_ticket())
            self.language.check_ticket(expiry)
        elif option == '4':
            funds = operation.system_funds_check(self.funds_check())
            self.language.funds_check(funds)
        elif option == '5':
            prepaidtickets = operation.system_prepaid_check(self.funds_check())
            self.language.prepaid_check(prepaidtickets)
        elif option == '6':
            self.problem_report()
        elif option == '7':
            self.language.terminate()
            time.sleep(3)
            self.terminate()
        else:
            operation.error_log(WrongOptionError)
            raise WrongOptionError
        time.sleep(4)
        self.language.terminate()
        self.terminate()

    def paper_ticket(self):
        '''
        Reads paper ticket type from
        ticket type function and reads full name
        of the customer from personal data function
        abd returns tuple (full name, ticket type).
        '''
        ticket_type = self.paper_ticket_type()
        name = self.personal_data()
        return (name, ticket_type)

    def paper_ticket_type(self):
        '''
        Reads input ticket type from
        customer and returns it.
        '''
        self.language.paper_ticket_type()
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

    def time_ticket_type(self):
        '''
        Reads input time  ticket type from
        customer and returns it.
        '''
        self.language.time_ticket_type()
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

    def funds_check(self):
        '''
        Returns full name from personal data
        function
        '''
        name = self.personal_data()
        return name

    def personal_data(self):
        '''
        Shows input messages from language
        interfaces, reads first name and
        last name of customer. Returns full
        name as a tuple.
    '''
        self.language.personal_data('first')
        fname = operation.choice()
        self.language.personal_data('last')
        lname = operation.choice()
        name = (fname, lname)
        return name

    def time_ticket(self):
        '''
        Reads choosen time ticket type
        and full name from functions
        and returns them in a tuple.
        '''
        ticket_type = self.time_ticket_type()
        name = self.personal_data()
        return (name, ticket_type)

    def problem_report(self):
        '''
        Shows problem report message
        from language interface. Then
        function puts typed problem message
        and runs error log function.
        '''
        self.language.problem_report()
        message = operation.choice()
        operation.error_log(None, message)
        self.language.operation_done()

    def check_ticket(self):
        '''
        Reads customer name from
        personal data function.
        '''
        name = self.personal_data()
        return name

    def terminate(self):
        pass


Ticket_prices = get_ticket_prices()
Databases = get_databases()
operation = machine_system(Databases, Ticket_prices)
interface = main_interface()

while True:
    try:
        interface.ticket_machine_init()
    except(WrongOptionError):
        interface.language.WrongOption()
        time.sleep(4)
        interface.terminate()
    except(MissingFileError):
        interface.language.MissingFile()
        time.sleep(4)
        interface.terminate()
    except(TimeTicketAlreadyExistsError):
        interface.language.TimeTicketExists()
        time.sleep(4)
        interface.terminate()
    except(NotEnoughMoneyError):
        interface.language.NotEnoughFunds()
        time.sleep(4)
        interface.terminate()
    except(PersonNotFoundError):
        interface.language.CustomerNotFound()
        time.sleep(4)
        interface.terminate()
    except(TicketDoesNotExistError):
        interface.language.TicketDoesNotExist()
        time.sleep(4)
        interface.terminate()
