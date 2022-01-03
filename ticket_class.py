class ticket:
    def __init__(self, info_list):
        ticket_id, ticket_type, ticket_date = info_list
        self.ticket_id = ticket_id
        self.ticket_type = ticket_type
        self.ticket_date = ticket_date