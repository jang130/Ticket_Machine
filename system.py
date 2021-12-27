from datetime import datetime, date, time
#from interface import time_ticket
from paper_ticket_class import ticket
from customer_class import customer
import os

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

class machine_system:
    def __init__(self):
        pass

    def system_ticket(self, ticket_info):
        name, ticket_type = ticket_info
        fname, lname = name
        time = self.time_module()[0]
        date = self.time_module()[1]
        #recieve format ((fname,lastname), ticket_type)
        #adds ticket to the database
        for person in self.people:
            if fname == person.fname and lname == person.lname:
                if person.ticket_type == 'None':
                    person.ticket_type = ticket_type
                    person.ticket_date = f'{time} {date}'
                    self.write_file('Customer_data')
                    return
                else:
                    raise TicketAlreadyExistsError

        raise PersonNotFoundError


    def system_check_ticket(self, name):
        fname = name[0]
        lname = name[1]
        for person in self.people:
            if fname == person.fname and lname == person.lname:
                if person.ticket_date != 'None':
                    time = person.ticket_date
                    time = self.date_split(time)
                    hour, minute, second, day, month, year = time
                    if person.ticket_type == '1m':
                        month += 1
                    elif person.ticket_type == '3m':
                        month +=3
                    elif person.ticket_type == '1y':
                        year +=1
                else:
                    raise TicketDoesNotExistError
        expiry = self.date_build(hour, minute, second, day, month, year)
        return expiry
#datetime wrong months
    def date_build(self, hour, minute, second, day, month, year ):
        time = f'{hour}:{minute}:{second}'
        date = f'{day}/{month}/{year}'
        return (time, date)

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

    def prepaid_check(self):
        pass

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
        #return (currenttime.isoformat(), currentdate.isoformat())

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
print(oper.system_check_ticket(('Jakob','Pettet')))