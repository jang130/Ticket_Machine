class customer:
    '''
    Class that represents customer. Read from
    Customer_data.txt
    '''
    def __init__(self, info_list):
        '''
        Initial method

        :param info_list:
        :type tuple:
        :format (id, fname, lname, ticket_id, funds)
        '''
        id, fname, lname, ticket_id, funds = info_list
        self.id = id
        self.fname = fname
        self.lname = lname
        self.ticket_id = ticket_id
        self.funds = funds
