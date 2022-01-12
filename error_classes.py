'''
error_classes contains classes with error exceptions
'''
class WrongOptionError(Exception):
    def __init__(self):
        super().__init__('Wrong choice')


class WrongAmountOfAtributesInClassError(Exception):
    def __init__(self):
        super().__init__('Cannot generate object wrong number of atributes')


class PersonNotFoundError(Exception):
    def __init__(self):
        super().__init__('Customer not found in database')


class TicketAlreadyExistsError(Exception):
    def __init__(self):
        super().__init__('Customer already have ticket')


class TicketDoesNotExistError(Exception):
    def __init__(self):
        super().__init__('Customer does not have ticket')


class TimeTicketAlreadyExistsError(Exception):
    def __init__(self):
        super().__init__('There can only be one time ticket')


class NotEnoughMoneyError(Exception):
    def __init__(self):
        super().__init__('Insufficient funds')


class MissingFileError(FileNotFoundError):
    def __init__(self):
        super().__init__('Data file not found')
