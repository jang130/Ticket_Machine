class ticket:
    '''
    Class that represents ticket. Read from
    Ticket_data.txt
    '''
    def __init__(self, info_list):
        '''
        Initial method

        :param info_list:
        :type tuple:
        :format (ticket_id, ticket_type, ticket_date)
        '''
        ticket_id, ticket_type, ticket_date = info_list
        self.ticket_id = ticket_id
        self.ticket_type = ticket_type
        self.ticket_date = ticket_date
