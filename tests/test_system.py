from system import machine_system

def test_system():
    machine = machine_system()

def test_machine_system_class(monkeypatch):
    syssstem = machine_system()
    class machine:
        def choice():
            return '2'


    #monkeypatch.setattr('system.machine_system.choice', choice())
    monkeypatch.setattr('system.machine_system', machine.choice())
    assert syssstem.choice() == '2'
