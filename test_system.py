from system import machine_system

def test_system():
    machine = machine_system()

def test_machine_system_class_any_ticket():
    operation = machine_system()
    operation.load_file('Customer_data')
    operation.tickets_load('Ticket_data') #dodać testowe bazy
    short_term_ticket =(('Doralyn','Dovermann'),'20min')
    time_ticket = (('Doralyn','Dovermann'),'1y')
    assert operation.system_ticket(short_term_ticket) == 'Succeed'
    assert operation.system_ticket(time_ticket) == 'Succeed'




    #monkeypatch.setattr('system.machine_system.choice', choice())
    #monkeypatch.setattr('system.machine_system', operation.choice())
    #assert operation.choice() == '2'
