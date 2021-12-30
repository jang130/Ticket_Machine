from system import machine_system
from interface import choose_language

def test_EN_interface_choice(monkeypatch):
    def choice():
        return '1'
    machine = machine_system()
    machine.choice()
    monkeypatch.setattr('system.choice', choice)
    assert choice() == '1'

def test_PL_interface_choice(monkeypatch):
    def choice():
        return '2'
    monkeypatch.setattr('interface.choose_language', choice)
    assert 1==1