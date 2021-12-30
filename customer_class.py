class IncorrectDataError(Exception):
    def __init__(self) -> None:
        super().__init__('This customer info is not correct')
class customer:
    def __init__(self, info_list):
        id, fname, lname, ticket_type, ticket_date, funds = info_list
        self.id = id
        self.fname = fname
        self.lname = lname
        self.ticket_type = ticket_type
        self.ticket_date = ticket_date
        self.funds = funds
