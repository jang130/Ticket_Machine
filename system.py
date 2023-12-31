from datetime import datetime, date
from customer_class import machine_customer
from ticket_class import machine_ticket
import os
from dateutil.relativedelta import relativedelta
from error_classes import MissingFileError, TimeTicketAlreadyExistsError
from error_classes import PersonNotFoundError, TicketDoesNotExistError
from error_classes import WrongAmountOfAtributesInClassError
from error_classes import NotEnoughMoneyError


class machine_system:
    '''
    System class that does all of
    the needed file and computing operations
    '''
    def __init__(self, Databases, Ticket_prices):
        self.ticket_data = Databases[0]
        self.customer_data = Databases[1]
        self.problem_report = Databases[5]
        self.pattern_ticket_data = Databases[3]
        self.pattern_customer_data = Databases[4]
        self.error_logs = Databases[6]
        self.Ticket_prices = Ticket_prices

    def system_ticket(self, ticket_info):
        '''
        System ticket is a method that have input information
        about customers full name and choosen ticket type.
        Based on that method buys a paper and time ticket and
        puts to the database.

        :param ticket_info:
        :type tuple:
        :format ((fname,lastname), ticket_type)
        fname, lname and ticket_type are strings.
        '''
        name, ticket_type = ticket_info
        fname, lname = name
        time = self.time_module()[0]
        date = self.time_module()[1]
        person_found = False
        for customer in self.customers:
            if fname == customer.fname and lname == customer.lname:
                if ticket_type in ('1m', '3m', '1y'):
                    exists = self.check_time_ticket_exists(customer)
                    if exists is not False:
                        self.error_log(TimeTicketAlreadyExistsError)
                        raise TimeTicketAlreadyExistsError
                ticket_id = self.unique_id()
                ticket_date = f'{time} {date}'
                ticket = machine_ticket((ticket_id, ticket_type, ticket_date))
                self.tickets.append(ticket)
                tickets = self.ticket_split(customer)
                tickets.append(ticket_id)
                customer.ticket_id = ';'.join(tickets)
                funds = customer.funds
                customer.funds = self.buy_ticket(funds, ticket_type)
                person_found = True
                self.write_file(self.customer_data)
                self.tickets_write(self.ticket_data)
                return 'Succeed'
        if person_found is False:
            self.error_log(PersonNotFoundError)
            raise PersonNotFoundError

    def system_check_ticket(self, name):
        '''
        System check ticket is a method that checks
        in the database expiry date of period type ticket

        :param name:
        :type tuple:
        :format (fname, lastname):
        fname and lname are strings.
        '''
        fname = name[0]
        lname = name[1]
        for customer in self.customers:
            if fname == customer.fname and lname == customer.lname:
                exists = self.check_time_ticket_exists(customer)
                if exists is not False:
                    expiry_dates = self.calculate_expiry_date(customer)
                    return expiry_dates
                else:
                    self.error_log(TicketDoesNotExistError)
                    raise TicketDoesNotExistError

    def check_time_ticket_exists(self, customer):
        '''
        check_time_ticket_exists is a method that takes customer object
        as an input data and checks if he or she already has time ticket.
        Every customer can have only one time ticket type at once.
        When ticket found then method returns this ticket object else it
        returns False.

        :param customer:
        :type object:
        '''
        customer_tickets = self.ticket_split(customer)
        for ticket in self.tickets:
            if ticket.ticket_id in (customer_tickets):
                if ticket.ticket_type in ('1m', '3m', '1y'):
                    return ticket
        return False

    def calculate_expiry_date(self, customer):
        '''
        calculate_expiry_date is a method that takes customer
        object as an input data and checks his time ticket
        bought date. Based on that and ticket type the method
        calculates the expiry date and returns as a datetime object

        :param customer:
        :type object:
        '''
        ticket = self.check_time_ticket_exists(customer)
        ticket_type = ticket.ticket_type
        time = ticket.ticket_date
        time = self.date_split(time)
        hour, minute, second, day, month, year = time
        time = datetime(year, month, day, hour, minute, second)
        if ticket_type == '1m':
            expiry = time + relativedelta(months=+1)
        elif ticket_type == '3m':
            expiry = time + relativedelta(months=+3)
        elif ticket_type == '1y':
            expiry = time + relativedelta(months=+12)
        else:
            self.error_log(TicketDoesNotExistError)
            raise TicketDoesNotExistError
        return expiry

    def ticket_split(self, customer):
        '''
        ticket_split is a method that reads customer object
        as an input data and checks ticket_id column.
        Based on that method splits ticket id's separated
        by ; sign and returns owned tickets list.
        Example [0,1,2,3]

        :param customer:
        :type object:
        '''
        ticket_id = customer.ticket_id
        ticket_id = ticket_id.split(';')
        return ticket_id

    def money_split(self, funds):
        '''
        money_split method is a method that uses funds in gr
        as an input and returns them as a tuple of zl and gr
        example: money(1625) returns (16, 25) input funds
        are gr and output are (zl, gr).

        :param funds:
        :type string:
        '''
        funds = int(funds)
        zl = funds // 100
        gr = funds % 100
        return (zl, gr)

    def charge_money(self, funds, cost):
        '''
        charge_money method does a money transaction.
        Input is a tuple of funds (zl, gr) and cost in gr.
        Method returns fund after fund/cost difference.
        example: charge_money((16,25),1325) does operation 16,25-13,25
        and returns 300 which means 300gr.

        :param funds:
        :type tuple:

        :param cost:
        :type int:
        '''
        zl = funds[0]
        gr = funds[1]
        costzl = cost // 100
        costgr = cost % 100
        zl = zl - costzl
        if zl < 0:
            self.error_log(NotEnoughMoneyError)
            raise NotEnoughMoneyError
        difference = costgr - gr
        gr = gr - costgr
        if gr < 0:
            zl -= 1
            gr = 100 - difference
        gr = zl*100 + gr
        funds = f"{gr}"
        return funds

    def buy_ticket(self, funds, ticket_type):
        '''
        buy_ticket is a method that checks the ticket type
        and based on that choose amount of money that will
        be taken from funds. Cost of each ticket is strictly
        precised in gr (grosz).

        :param funds:
        :type int:

        :param ticket_type:
        :type string:
        '''
        funds = self.money_split(funds)
        if ticket_type == '20min':
            funds = self.charge_money(funds, self.Ticket_prices[0])
        elif ticket_type == '75min':
            funds = self.charge_money(funds, self.Ticket_prices[1])
        elif ticket_type == '24h':
            funds = self.charge_money(funds, self.Ticket_prices[2])
        elif ticket_type == '72h':
            funds = self.charge_money(funds, self.Ticket_prices[3])
        elif ticket_type == '1m':
            funds = self.charge_money(funds, self.Ticket_prices[4])
        elif ticket_type == '3m':
            funds = self.charge_money(funds, self.Ticket_prices[5])
        elif ticket_type == '1y':
            funds = self.charge_money(funds, self.Ticket_prices[6])
        return funds

    def date_split(self, time):
        '''
        date_split is a helping method to the formatting
        date loaded from database. Method cuts given time in
        str formatt and puts each value to the specified variable.
        If input is for example 12:04:35 28/12/2021
        then it returns (12,4,35,28,12,2021)

        :param time:
        :type string:
        :format "hour:minute:second day,month,year":
        '''
        validity = time.split(' ')
        time, date = validity
        time = time.split(':')
        hour, minute, second = time
        date = date.split('/')
        day, month, year = date
        hour = int(hour)
        minute = int(minute)
        second = int(second)
        day = int(day)
        month = int(month)
        year = int(year)
        return (hour, minute, second, day, month, year)

    def unique_id(self):
        '''
        unique_id is a method that returns to each
        bought ticket id that none previous ticket had.
        The id's are growing one by one.
        '''
        id = 0
        for ticket in self.tickets:
            id = str(id)
            if ticket.ticket_id == id:
                id = int(id)
                id += 1
        return str(id)

    def system_prepaid_check(self, name):
        '''
        system_prepaid_check is a method that takes name
        in (fname, lname) tuple and seraches in data base matching
        customer, then the customer is runned in the finding method.
        After finding tickets id's function returns theese tickets.

        :param name:
        :type tuple:
        '''
        fname = name[0]
        lname = name[1]
        for customer in self.customers:
            if fname == customer.fname and lname == customer.lname:
                prepaid_tickets = self.find_prepaid_tickets(customer)
                if len(prepaid_tickets) == 0:
                    self.error_log(TicketDoesNotExistError)
                    raise TicketDoesNotExistError
                else:
                    return prepaid_tickets
        self.error_log(PersonNotFoundError)
        raise PersonNotFoundError

    def find_prepaid_tickets(self, customer):
        '''
        find_prepaid_tickets is a method that takes name
        in (fname, lname) tuple and searches for prepaid tickets
        under given customer's object. Found tickets are added to a list
        and returned.

        :param customer:
        :type object:
        '''
        customer_tickets = self.ticket_split(customer)
        prepaid_tickets = []
        for ticket in self.tickets:
            if ticket.ticket_id in (customer_tickets):
                if ticket.ticket_type.isdigit():
                    prepaid_tickets.append(ticket.ticket_type)
        return prepaid_tickets

    def system_funds_check(self, name):
        '''
        system_funds_check is a method that checks the amount of
        funds in database for a given customer and using one functionality
        from money method returns funds splitted to zl (złoty) and gr (grosz).

        :param name:
        :type tuple:
        :format (fname, lname):
        fname and lname are strings.
        '''
        fname = name[0]
        lname = name[1]
        for person in self.customers:
            if fname == person.fname and lname == person.lname:
                return self.money_split(person.funds)
        self.error_log(PersonNotFoundError)
        raise PersonNotFoundError

    def choice(self):
        '''
        choice is a method that takes user input
        as string.
        '''
        choice_input = str(input())
        return choice_input

    def time_module(self, issecond=None):
        '''
        time_module is double option method that
        returns formatted current time and date from system.
        If is second is False then time is returned in hour:minute format.
        If issecond is None time is returned in hour:minute:second format.

        :param issecond:
        :type boolean (False):
        '''
        currenttime = datetime.now()
        currentdate = date.today()
        if issecond is False:
            formatted_date = currentdate.strftime("%d/%m/%Y")
            formatted_time = currenttime.strftime("%H:%M")
        else:
            formatted_date = currentdate.strftime("%d/%m/%Y")
            formatted_time = currenttime.strftime("%H:%M:%S")
        return (formatted_time, formatted_date)

    def clear_console(self):
        '''
        clear_console is a method that clears system terminal.
        '''
        clear = lambda: os.system('clear')
        return clear()

    def load_file(self, path):
        '''
        load_file is a method that reads database file from
        given path and creates list of customer's objects.
        Used to read Customer_data.

        :param path:
        :type string:
        '''
        try:
            with open(path, 'r') as data_file:
                self.customers = []
                data_file.readline()
                for line in data_file:
                    line = line.rstrip()
                    columns = line.split(',')
                    id, fname, lname, ticket_id, funds = columns
                    person = machine_customer(columns)
                    self.customers.append(person)
        except FileNotFoundError:
            self.error_log(MissingFileError)
            raise MissingFileError

    def error_log(self, error=None, message=None):
        '''
        problem_report is  a method that saves actual state of machine
        and does the error report file. When the error attribute contains
        error Error_log is being updatet with a new error with a time stamp.
        When the message contains text. Method is cloning Error_log
        and putting inside describing problem message which
        generates to Problem_report.txt.

        :param error:
        :type error class:

        :param message:
        :type string:
        '''
        time = self.time_module()[0]
        date = self.time_module()[1]
        try:
            with open(self.error_logs, "r") as log:
                data = log.read()
            if message is None:
                error = str(error)
                with open(self.error_logs, "w") as log:
                    log.write(data)
                    log.write(f'\n{time} {date} Error:{error}')
            elif error is None:
                with open(self.problem_report, "w") as log:
                    log.write(f'\n{message}\n\r')
                    log.write(data)
        except FileNotFoundError:
            self.error_log(MissingFileError)
            raise MissingFileError
        except ValueError:
            self.error_log(WrongAmountOfAtributesInClassError)
            raise WrongAmountOfAtributesInClassError

    def write_file(self, path):
        '''
        write_file is a method thats overwrites Customer_data with
        updated informations.

        :param path:
        :type string:

        '''
        with open(path, 'w') as data_file:
            data_file.write('id,first_name,last_name,ticket_id,funds\n')
            for person in self.customers:
                id = person.id
                fname = person.fname
                lname = person.lname
                ticket_id = person.ticket_id
                funds = person.funds
                line = f'{id},{fname},{lname},{ticket_id},{funds}\n'
                data_file.write(line)

    def tickets_load(self, path):
        '''
        tickets_file is a method that reads ticket database file from
        given path and creates list of ticket's objects.
        Used to read Ticket_data.

        :param path:
        :type string:
        '''
        try:
            with open(path, 'r') as tickets_file:
                self.tickets = []
                tickets_file.readline()
                for line in tickets_file:
                    line = line.rstrip()
                    columns = line.split(',')
                    ticket_id, ticket_type, ticket_date = columns
                    ticket_unit = machine_ticket(columns)
                    self.tickets.append(ticket_unit)
        except FileNotFoundError:
            self.error_log(MissingFileError)
            raise MissingFileError
        except ValueError:
            self.error_log(WrongAmountOfAtributesInClassError)
            raise WrongAmountOfAtributesInClassError

    def tickets_write(self, path):
        '''
        tickets_write is a method that overwrites ticket_data
        with a new tickets (if available).
        '''
        with open(path, 'w') as tickets_file:
            tickets_file.write('ticket_id,ticket_type,ticket_date\n')
            for ticket in self.tickets:
                ticket_id = ticket.ticket_id
                ticket_type = ticket.ticket_type
                ticket_date = ticket.ticket_date
                line = f'{ticket_id},{ticket_type},{ticket_date}\n'
                tickets_file.write(line)

    def files_reset(self):
        '''
        file_reset is a method that clears Ticket_data from tickets
        and Customers_data from ticket_id. Customer_data is being
        overwirtten by Pattern_customer_data. Which contains sample
        database of customers with id's,names and funds.
        '''
        with open(self.pattern_ticket_data, "r") as reset:
            data = reset.read()
        with open(self.ticket_data, 'w') as reset:
            reset.write(data)
        with open(self.pattern_customer_data, "r") as reset:
            data = reset.read()
        with open(self.customer_data, "w") as reset:
            reset.write(data)
