from os import name
from system import NotEnoughMoneyError, TicketAlreadyExistsError, TimeTicketAlreadyExistsError, machine_system
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


def test_machine_system_class_check_time_ticket_and_calc_expiry():
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

def test_ticket_split():
    operation = machine_system()
    operation.files_reset()
    operation.load_file('Customer_data')
    operation.tickets_load('Ticket_data')
    ticket1 = (('Doralyn','Dovermann'),'20min')
    ticket2 = (('Doralyn','Dovermann'),'75min')
    ticket3 = (('Doralyn','Dovermann'),'24h')
    operation.system_ticket(ticket1)
    operation.system_ticket(ticket2)
    operation.system_ticket(ticket3)
    customer = operation.customers[0]
    ticket_split = operation.ticket_split(customer)
    assert ticket_split == ['', '0', '1', '2']


def test_money_split():
    operation = machine_system()
    funds=1800
    for i in range(100):
        money_split = operation.money_split(funds)
        assert money_split == (18,i)
        funds +=1


def test_charge_money():
    operation = machine_system()
    funds = (15, 50)
    cost = 1230
    charge_money = operation.charge_money(funds, cost)
    assert charge_money == ('320')

def test_charge_money_insufficient_funds():
    operation = machine_system()
    funds = (15, 50)
    cost = 1600
    with pytest.raises(NotEnoughMoneyError):
        operation.charge_money(funds, cost)

def test_buy_ticket_method():
    operation = machine_system()
    buy_ticket1 = operation.buy_ticket('15000','20min')
    buy_ticket2 = operation.buy_ticket('15000','75min')
    buy_ticket3 = operation.buy_ticket('15000','24h')
    buy_ticket4 = operation.buy_ticket('15000','72h')
    assert buy_ticket1 == '14660'
    assert buy_ticket2 == '14560'
    assert buy_ticket3 == '13500'
    assert buy_ticket4 == '11400'


def test_buy_ticket_method_insufficient_funds():
    operation = machine_system()
    with pytest.raises(NotEnoughMoneyError):
        operation.buy_ticket('1500', '72h')

def test_date_split_method():
    operation = machine_system()
    date_split = operation.date_split('12:04:35 28/12/2021')
    assert date_split == (12,4,35,28,12,2021)


def test_unique_id_for_ticket_method():
    operation = machine_system()
    operation.files_reset()
    operation.load_file('Customer_data')
    operation.tickets_load('Ticket_data')
    assert operation.unique_id() == '0'




    #monkeypatch.setattr('system.machine_system.choice', choice())
    #monkeypatch.setattr('system.machine_system', operation.choice())
    #assert operation.choice() == '2'
#operation.write_file('Customer_data')
#operation.tickets_write('Ticket_data')