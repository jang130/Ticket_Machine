
from system import NotEnoughMoneyError, PersonNotFoundError, machine_system
from system import TicketDoesNotExistError, TimeTicketAlreadyExistsError
from system import MissingFileError
import pytest
import io
from datetime import datetime, date
from settings import get_databases

Databases = get_databases()
ticket_data = Databases[0]
customer_data = Databases[1]


def test_system():
    machine_system(Databases)


def test_machine_system_class_buy_any_ticket():
    operation = machine_system(Databases)
    operation.files_reset()
    operation.load_file(customer_data)
    operation.tickets_load(ticket_data)
    short_term_ticket = (('Doralyn', 'Dovermann'), '20min')
    short_term_ticket2 = (('Doralyn', 'Dovermann'), '24h')
    time_ticket = (('Doralyn', 'Dovermann'), '1y')
    assert operation.system_ticket(short_term_ticket) == 'Succeed'
    assert operation.system_ticket(short_term_ticket2) == 'Succeed'
    assert operation.system_ticket(time_ticket) == 'Succeed'


def test_machine_system_class_buy_two_time_tickets():
    operation = machine_system(Databases)
    operation.files_reset()
    operation.load_file(customer_data)
    operation.tickets_load(ticket_data)
    time_ticket = (('Doralyn', 'Dovermann'), '1y')
    with pytest.raises(TimeTicketAlreadyExistsError):
        assert operation.system_ticket(time_ticket) == 'Succeed'
        assert operation.system_ticket(time_ticket) == 'Succeed'


def test_machine_system_class_check_time_ticket_and_calc_expiry():
    operation = machine_system(Databases)
    operation.files_reset()
    operation.load_file(customer_data)
    operation.tickets_load(ticket_data)
    time_ticket = (('Doralyn', 'Dovermann'), '1y')
    customer = operation.customers[0]
    assert operation.system_ticket(time_ticket) == 'Succeed'
    name = (('Doralyn', 'Dovermann'))
    check_ticket = operation.system_check_ticket(name)
    expiry = operation.calculate_expiry_date(customer)
    assert check_ticket == expiry


def test_ticket_split():
    operation = machine_system(Databases)
    operation.files_reset()
    operation.load_file(customer_data)
    operation.tickets_load(ticket_data)
    ticket1 = (('Doralyn', 'Dovermann'), '20min')
    ticket2 = (('Doralyn', 'Dovermann'), '75min')
    ticket3 = (('Doralyn', 'Dovermann'), '24h')
    operation.system_ticket(ticket1)
    operation.system_ticket(ticket2)
    operation.system_ticket(ticket3)
    customer = operation.customers[0]
    ticket_split = operation.ticket_split(customer)
    assert ticket_split == ['1', '2', '3', '4']


def test_money_split():
    operation = machine_system(Databases)
    funds = 1800
    for i in range(100):
        money_split = operation.money_split(funds)
        assert money_split == (18, i)
        funds += 1


def test_charge_money():
    operation = machine_system(Databases)
    funds = (15, 50)
    cost = 1230
    charge_money = operation.charge_money(funds, cost)
    assert charge_money == ('320')


def test_charge_money_insufficient_funds():
    operation = machine_system(Databases)
    funds = (15, 50)
    cost = 1600
    with pytest.raises(NotEnoughMoneyError):
        operation.charge_money(funds, cost)


def test_buy_ticket_method():
    operation = machine_system(Databases)
    buy_ticket1 = operation.buy_ticket('15000', '20min')
    buy_ticket2 = operation.buy_ticket('15000', '75min')
    buy_ticket3 = operation.buy_ticket('15000', '24h')
    buy_ticket4 = operation.buy_ticket('15000', '72h')
    assert buy_ticket1 == '14660'
    assert buy_ticket2 == '14560'
    assert buy_ticket3 == '13500'
    assert buy_ticket4 == '11400'


def test_buy_ticket_method_insufficient_funds():
    operation = machine_system(Databases)
    with pytest.raises(NotEnoughMoneyError):
        operation.buy_ticket('1500', '72h')


def test_date_split_method():
    operation = machine_system(Databases)
    date_split = operation.date_split('12:04:35 28/12/2021')
    assert date_split == (12, 4, 35, 28, 12, 2021)


def test_unique_id_for_ticket_method():
    operation = machine_system(Databases)
    operation.files_reset()
    operation.load_file(customer_data)
    operation.tickets_load(ticket_data)
    assert operation.unique_id() == '2'


def test_system_prepaid_check_method():
    operation = machine_system(Databases)
    operation.files_reset()
    operation.load_file(customer_data)
    operation.tickets_load(ticket_data)
    prepaid = operation.system_prepaid_check(('Doralyn', 'Dovermann'))
    assert prepaid == ['26']


def test_system_prepaid_check_method_missing_person():
    operation = machine_system(Databases)
    operation.files_reset()
    operation.load_file(customer_data)
    operation.tickets_load(ticket_data)
    with pytest.raises(PersonNotFoundError):
        operation.system_prepaid_check(('Doralyn', 'Doralyn'))


def test_system_prepaid_check_method_missing_ticket():
    operation = machine_system(Databases)
    operation.files_reset()
    operation.load_file(customer_data)
    operation.tickets_load(ticket_data)
    with pytest.raises(TicketDoesNotExistError):
        operation.system_prepaid_check(('Whitney', 'Girardoni'))


def test_system_funds_check_method():
    operation = machine_system(Databases)
    operation.files_reset()
    operation.load_file(customer_data)
    operation.tickets_load(ticket_data)
    funds = operation.system_funds_check(('Whitney', 'Girardoni'))
    assert funds == (1000, 0)


def test_system_funds_check_method_missing_person():
    operation = machine_system(Databases)
    operation.files_reset()
    operation.load_file(customer_data)
    operation.tickets_load(ticket_data)
    with pytest.raises(PersonNotFoundError):
        operation.system_funds_check(('Whitney', 'Whitney'))


def test_choice(monkeypatch):
    operation = machine_system(Databases)
    monkeypatch.setattr('sys.stdin', io.StringIO('1'))
    choice = operation.choice()
    assert choice == '1'
    monkeypatch.setattr('sys.stdin', io.StringIO('2'))
    choice = operation.choice()
    assert choice == '2'


def test_time_module():
    operation = machine_system(Databases)
    today = date.today().strftime("%d/%m/%Y")
    time = datetime.now().strftime("%H:%M")
    assert operation.time_module(False) == (time, today)
    today = date.today().strftime("%d/%m/%Y")
    time = datetime.now().strftime("%H:%M:%S")
    assert operation.time_module(True) == (time, today)


def test_load_file():
    operation = machine_system(Databases)
    operation.files_reset()
    operation.load_file(customer_data)


def test_load_wrong_file():
    operation = machine_system(Databases)
    operation.files_reset()
    with pytest.raises(MissingFileError):
        operation.load_file('Customer_datatata')


def test_write_file():
    operation = machine_system(Databases)
    operation.files_reset()
    operation.load_file(customer_data)
    operation.write_file(customer_data)


def test_tickets_load():
    operation = machine_system(Databases)
    operation.tickets_load(ticket_data)


def test_tickets_load_wrong_file():
    operation = machine_system(Databases)
    with pytest.raises(MissingFileError):
        operation.tickets_load('Ticket_datatata')


def test_tickets_write():
    operation = machine_system(Databases)
    operation.tickets_load(ticket_data)
    operation.tickets_write(ticket_data)


def test_error_log_check():
    operation = machine_system(Databases)
    operation.error_log(MissingFileError)


def test_error_log_check_problem_report():
    operation = machine_system(Databases)
    operation.error_log('Sample error description')


def test_reset_files():
    operation = machine_system(Databases)
    operation.files_reset()
