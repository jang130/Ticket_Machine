from datetime import datetime, date, time
from paper_ticket_class import ticket
from customer_class import customer
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

class machine_system:
    def __init__(self):
        pass

    def system_ticket(self, ticket_info):
        #recieve format ((fname,lastname), ticket_type)
        #adds ticket to the database
        name, ticket_type = ticket_info
        fname, lname = name
        time = self.time_module()[0]
        date = self.time_module()[1]
        for person in self.people:
            if fname == person.fname and lname == person.lname:
                if person.ticket_type == 'None':
                    funds = person.funds
                    person.ticket_type = ticket_type
                    person.ticket_date = f'{time} {date}'
                    person.funds = self.buy_ticket(funds, ticket_type)
                    self.write_file('Customer_data')
                    return
                else:
                    raise TicketAlreadyExistsError

        raise PersonNotFoundError


    def system_check_ticket(self, name):
        fname = name[0]
        lname = name[1]
        expiry = 0
        for person in self.people:
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
                        raise IsNotTimeTicketError
                else:
                    raise TicketDoesNotExistError
        if expiry != 0:
            return expiry
        else:
            raise PersonNotFoundError

    def money(self, funds, cost=None):
        funds = int(funds)
        zl = funds // 100
        gr = funds % 100
        if cost is None:
            return (zl, gr)

        costzl = cost // 100
        costgr = cost % 100
        zl = zl - costzl
        if zl < 0:
            raise NotEnoughMoneyError
        difference = costgr - gr
        gr = gr - costgr
        if gr < 0:
            zl -= 1
            gr =  100 - difference
        funds = f"{zl}{gr}"
        return funds


    def buy_ticket(self, funds, ticket_type):
        if ticket_type == '20min':
            funds = self.money(funds, 340)
        elif ticket_type == '75min':
            funds = self.money(funds, 340)
        elif ticket_type == '24h':
            funds = self.money(funds, 340)
        elif ticket_type == '72h':
            funds = self.money(funds, 340)
        elif ticket_type == '1m':
            funds = self.money(funds, 340)
        elif ticket_type == '3m':
            funds = self.money(funds, 340)
        elif ticket_type == '1y':
            funds = self.money(funds, 340)
        return funds


    def date_split(self, time):
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
        fname = name[0]
        lname = name[1]
        for person in self.people:
            if fname == person.fname and lname == person.lname:
                return self.money(person.funds)
        raise PersonNotFoundError

    def problem_report(self):
        pass

    def choice(self):
        choice_input = str(input())
        return choice_input

    def time_module(self):
        currenttime = datetime.now()
        currentdate = date.today()
        formatted_date = currentdate.strftime("%d/%m/%Y")
        formatted_time = currenttime.strftime("%H:%M:%S")
        return (formatted_time, formatted_date)


    def clear_console(self):
        clear = lambda: os.system('clear')
        return clear()

    def load_file(self, path):
        with open(path, 'r') as data_file:
            self.people = []
            data_file.readline()
            for line in data_file:
                line = line.rstrip()
                columns = line.split(',')
                id, fname, lname, ticket_type, ticket_date, funds = columns
                person = customer(columns)
                self.people.append(person)

    def write_file(self, path):
        with open(path, 'w') as data_file:
            data_file.write('id,first_name,last_name,ticket_type,ticket_date,funds\n')
            for person in self.people:
                id = person.id
                fname = person.fname
                lname = person.lname
                ticket_type = person.ticket_type
                ticket_date = person.ticket_date
                funds = person.funds
                line = f'{id},{fname},{lname},{ticket_type},{ticket_date},{funds}\n'
                data_file.write(line)

oper = machine_system()
oper.load_file('Customer_data')
#print(oper.money(1144,5522))


