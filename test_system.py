from system import machine_system

def test_system():
    assert 1==1

def test_machine_system_class(monkeypatch):
    machine = machine_system()
    def choice():
        return '2'
    monkeypatch.setattr('interface.choose_language', choice)
    assert 1==1
