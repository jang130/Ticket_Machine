class WrongOptionError(Exception):
    def __init__(self):
        super().__init__('Wrong choice')

def language():
    pass

def paper_ticket():
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
    choice_input = int(input())
    return choice_input