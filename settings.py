def get_databases():
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