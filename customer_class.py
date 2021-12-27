class IncorrectDataError(Exception):
    def __init__(self) -> None:
        super().__init__('This customer info is not correct')
class customer:
    def __init__(self, info_list):
        id, first_name, last_name, ticket_type, ticket_date, funds = info_list
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.ticket_type = ticket_type
        self.ticket_date = ticket_date
        self.funds = funds
