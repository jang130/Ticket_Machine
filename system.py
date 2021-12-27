from datetime import datetime, date, time
from paper_ticket_class import ticket
from customer_class import customer
import os
class WrongOptionError(Exception):
    def __init__(self):
        super().__init__('Wrong choice')

def system_ticket(ticket_info):
    #recieve format ((fname,lastname), ticket_type)
    #adds ticket to the database
    pass


def time_ticket():
    pass


def ticket_valid():
    pass


def prepaid_check():
    pass

def problem_report():
    pass

def choice():
    choice_input = str(input())
    return choice_input

def time_module():
    currenttime = datetime.now()
    currentdate = date.today()
    formatted_date = currentdate.strftime("%d/%m/%Y")
    formatted_time = currenttime.strftime("%H:%M:%S")
    return (formatted_time, formatted_date)

def clear_console():
    clear = lambda: os.system('clear')
    return clear()

def load_file(path):
    with open(path, 'r') as data_file:
        people = []
        data_file.readline()
        for line in data_file:
            line = line.rstrip()
            columns = line.split(',')
            id, first_name, last_name, ticket_type, ticket_date, funds = columns
            person = customer(columns)
            people.append(person)
    for person in people:
        print(person.ticket_date)


print(load_file('Customer_data'))