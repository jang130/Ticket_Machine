class IncorrectDataError(Exception):
    def __init__(self) -> None:
        super().__init__('This customer info is not correct')

class customer:
    def __init__(self, info_list):
        id, fname, lname, ticket_id, funds = info_list
        self.id = id
        self.fname = fname
        self.lname = lname
        self.ticket_id = ticket_id
        self.funds = funds
