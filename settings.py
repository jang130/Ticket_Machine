def get_databases():
    '''
    Paths to databases
    '''
    ticket_data = 'Databases/Ticket_data'
    customer_data = 'Databases/Customer_data'
    pattern_customer_data = 'Databases/Pattern_Customer_data'
    pattern_ticket_data = 'Databases/Pattern_Ticket_data'
    problem_report = 'Databases/Problem_report'
    error_logs = 'Databases/Error_logs'
    output = [ticket_data, customer_data, pattern_customer_data]
    output.append(pattern_ticket_data)
    output.append(pattern_customer_data)
    output.append(problem_report)
    output.append(error_logs)
    return output


def get_ticket_prices():
    '''
    Ticket type prices
    '''
    minutes20 = 340
    minutes75 = 440
    hours24 = 1500
    hours72 = 3600
    month1 = 11000
    month3 = 28000
    year1 = 44000
    output = [minutes20, minutes75, hours24, hours72]
    output.append(month1)
    output.append(month3)
    output.append(year1)
    return output
