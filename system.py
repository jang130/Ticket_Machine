from datetime import datetime, date, time
from paper_ticket_class import ticket
from customer_class import customer
import os

class WrongOptionError(Exception):
    def __init__(self):
        super().__init__('Wrong choice')
class PersonNotFoundError(Exception):
    def __init__(self):
        super().__init__('Customer not found in database')

class machine_system:
    def __init__(self):
        pass

    def system_ticket(self, ticket_info):
        name, ticket_type = ticket_info
        fname, lname = name
        #recieve format ((fname,lastname), ticket_type)
        #adds ticket to the database
        for person in self.people:
            if fname == person.first_name:
                if lname == person.last_name:
                    #write ticket type and date to file
            else:
                raise PersonNotFoundError


    def time_ticket(self):
        pass


    def ticket_valid(self):
        pass


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
                id, first_name, last_name, ticket_type, ticket_date, funds = columns
                person = customer(columns)
                self.people.append(person)

#load_file('Customer_data')
