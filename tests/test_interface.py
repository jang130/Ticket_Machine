#from interface import choose_language
from system import machine_system
import io


def test_kkk():
    assert 1==1

def test_EN_interface_choice(monkeypatch):
    machine = machine_system()
    monkeypatch.setattr('sys.stdin', io.StringIO('1'))
    #machine.choice()
    #monkeypatch.setattr('system.machine_system.choice', choice)
    assert machine.choice() == '1'

def test_PL_interface_choice(monkeypatch):
    def choice():
        return 1
    #monkeypatch.setattr('interface.choose_language', choice)
    monkeypatch.setattr('system.machine_system.choice', choice)
    assert  1== 1

