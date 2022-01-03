from datetime import datetime, date
from time import time
from customer_class import customer
from ticket_class import ticket
import os
from datetime import datetime
from dateutil.relativedelta import relativedelta



class WrongOptionError(Exception):
    def __init__(self):
        super().__init__('Wrong choice')


class PersonNotFoundError(Exception):
    def __init__(self):
        super().__init__('Customer not found in database')


class TicketAlreadyExistsError(Exception):
    def __init__(self):
        super().__init__('Customer already have ticket')


class TicketDoesNotExistError(Exception):
    def __init__(self):
        super().__init__('Customer does not have ticket')


class IsNotTimeTicketError(Exception):
    def __init__(self):
        super().__init__('Ticket is not a period ticket')


class NotEnoughMoneyError(Exception):
    def __init__(self):
        super().__init__('Insufficient funds')


class MissingFileError(FileNotFoundError):
    def __init__(self):
        super().__init__('Data file not found')


class machine_system:
    '''
    System class that does all of
    the needed file and computing operations
    '''
    def __init__(self):
        pass

    def system_ticket(self, ticket_info):
        '''
        System ticket is a method that have input information
        about customers full name and choosen ticket type.
        Based on that method buys a ticket and puts to the database.

        :param ticket_info:
        :type tuple:
        :format ((fname,lastname), ticket_type)
        fname, lname and ticket_type are strings.
        '''
        name, ticket_type = ticket_info
        fname, lname = name
        time = self.time_module()[0]
        date = self.time_module()[1]
        for person in self.customers:
            if fname == person.fname and lname == person.lname:
                funds = person.funds
                tickets =  self.ticket_split(person)
                person.funds = self.buy_ticket(funds, ticket_type)
                self.write_file('Customer_data')
                return


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
        expiry = 0
        for person in self.customers:
            if fname == person.fname and lname == person.lname:
                if person.ticket_date != 'None':
                    time = person.ticket_date
                    time = self.date_split(time)
                    hour, minute, second, day, month, year = time
                    time = datetime(year, month, day, hour, minute, second)
                    if person.ticket_type == '1m':
                        expiry = time + relativedelta(months=+1)
                    elif person.ticket_type == '3m':
                        expiry = time + relativedelta(months=+3)
                    elif person.ticket_type == '1y':
                        expiry = time + relativedelta(months=+12)
                    elif person.ticket_type in ('20min', '75min', '24h', '72h'):
                        self.error_log(IsNotTimeTicketError)
                        raise IsNotTimeTicketError
                else:
                    self.error_log(TicketDoesNotExistError)
                    raise TicketDoesNotExistError
        if expiry != 0:
            return expiry
        else:
            self.error_log(PersonNotFoundError)
            raise PersonNotFoundError

    def ticket_split(self, person):
            ticket_id = person.ticket_id
            ticket_id = ticket_id.split(' ')
            return ticket_id

    def money_split(self, funds):
        funds = int(funds)
        zl = funds // 100
        gr = funds % 100
        return (zl, gr)

    def charge_money(self, funds, cost):
        '''
        money method is a method with double task.
        When cost is None the function returns funds
        example: money(1625) returns (16, 25) input funds
        are gr and output are (zl, gr).
        When cost is a number it returns the amount of funds
        after cost difference.
        example: money(1625,1325) does operation 16,25-13,25
        and returns 30 which means 30gr

        :param funds:
        :type int:

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
            funds = self.charge_money(funds, 340)
        elif ticket_type == '75min':
            funds = self.charge_money(funds, 340)
        elif ticket_type == '24h':
            funds = self.charge_money(funds, 340)
        elif ticket_type == '72h':
            funds = self.charge_money(funds, 340)
        elif ticket_type == '1m':
            funds = self.charge_money(funds, 340)
        elif ticket_type == '3m':
            funds = self.charge_money(funds, 340)
        elif ticket_type == '1y':
            funds = self.charge_money(funds, 340)
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

    def system_prepaid_check(self, name):
        '''
        system_prepaid_check is a method that checks the amount of
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
                return self.money(person.funds)
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
        given path and it create list of customer's objects.
        used to read Customer_data.

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
                    person = customer(columns)
                    self.customers.append(person)
        except FileNotFoundError:
            self.error_log(MissingFileError)
            raise MissingFileError

    def error_log(self, error=None, message=None):
        '''
        problem_report is  a method that saves actual state of machine
        and does the error report file.
        '''
        time = self.time_module()[0]
        date = self.time_module()[1]
        try:
            with open('Error_logs', "r") as log:
                data = log.read()
            if message is  None:
                error = str(error)
                with open('Error_logs', "w") as log:
                    log.write(data)
                    log.write(f'\n{time} {date} Error:{error}')
            elif error is None:
                with open('Problem_report', "w") as log:
                        log.write(f'\n{message}')
                        log.write(data)
            else:
                pass
        except FileNotFoundError:
            self.error_log(MissingFileError)
            raise MissingFileError

    def write_file(self, path):
        '''
        write_file is a method thats overwrites Customer_data with
        updated informations.

        :param path:
        :type string:

        '''
        with open(path, 'w') as data_file:
            data_file.write('id,first_name,last_name,ticket_type,ticket_date,funds\n')
            for person in self.customers:
                id = person.id
                fname = person.fname
                lname = person.lname
                ticket_id = person.ticket_id
                funds = person.funds
                line = f'{id},{fname},{lname},{ticket_id},{funds}\n'
                data_file.write(line)

    def tickets_load(self, path):
        try:
            with open(path, 'r') as tickets_file:
                self.tickets = []
                tickets_file.readline()
                for line in tickets_file:
                    line = line.rstrip()
                    columns = line.split(',')
                    ticket_id, ticket_type, ticket_date = columns
                    ticket = ticket(columns)
                    self.tickets.append(ticket)
        except FileNotFoundError:
            self.error_log(MissingFileError)
            raise MissingFileError

    def tickets_write(self, path):
        with open(path, 'w') as tickets_file:
            tickets_file.write('ticket_id,ticket_type,ticket_date\n')
            for ticket in self.tickets:
                ticket_id = ticket.ticket_id
                ticket_type = ticket.ticket_type
                ticket_date = ticket_date
                funds = ticket.funds
                line = f'{ticket_id},{ticket_type},{ticket_date},{funds}\n'
                tickets_file.write(line)
'''
'''
oper = machine_system()
#oper.error_log('Customer_data')
#message = 'jkaxsca'
#oper.error_log(None, message)
#oper.tickets_load('Ticket_data')
#oper.load_file('Customer_data')
#print(oper.ticket_split(oper.customers[0]))
#print(oper.money(1625,1623))


