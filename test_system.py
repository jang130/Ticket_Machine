from os import name
from system import TicketAlreadyExistsError, TimeTicketAlreadyExistsError, machine_system
import pytest

def test_system():
    machine = machine_system()

def test_machine_system_class_buy_any_ticket():
    operation = machine_system()
    operation.files_reset()
    operation.load_file('Customer_data')
    operation.tickets_load('Ticket_data')
    short_term_ticket =(('Doralyn','Dovermann'),'20min')
    short_term_ticket2 =(('Doralyn','Dovermann'),'24h')
    time_ticket = (('Doralyn','Dovermann'),'1y')
    assert operation.system_ticket(short_term_ticket) == 'Succeed'
    assert operation.system_ticket(short_term_ticket2) == 'Succeed'
    assert operation.system_ticket(time_ticket) == 'Succeed'

def test_machine_system_class_buy_two_time_tickets():
    operation = machine_system()
    operation.files_reset()
    operation.load_file('Customer_data')
    operation.tickets_load('Ticket_data')
    time_ticket = (('Doralyn','Dovermann'),'1y')
    with pytest.raises(TimeTicketAlreadyExistsError):
        assert operation.system_ticket(time_ticket) == 'Succeed'
        assert operation.system_ticket(time_ticket) == 'Succeed'


def test_machine_system_class_check_time_ticket():
    operation = machine_system()
    operation.files_reset()
    operation.load_file('Customer_data')
    operation.tickets_load('Ticket_data')
    time_ticket = (('Doralyn','Dovermann'),'1y')
    customer = operation.customers[0]
    assert operation.system_ticket(time_ticket) == 'Succeed'
    name = (('Doralyn','Dovermann'))
    check_ticket = operation.system_check_ticket(name)
    expiry = operation.calculate_expiry_date(customer)
    assert check_ticket == expiry







    #monkeypatch.setattr('system.machine_system.choice', choice())
    #monkeypatch.setattr('system.machine_system', operation.choice())
    #assert operation.choice() == '2'
#operation.write_file('Customer_data')
#operation.tickets_write('Ticket_data')