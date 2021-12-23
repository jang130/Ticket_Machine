from datetime import datetime, date, time
import os
class WrongOptionError(Exception):
    def __init__(self):
        super().__init__('Wrong choice')

def paper_ticket():
    #otrzymanie krotki z typem biletu i iloscią
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
