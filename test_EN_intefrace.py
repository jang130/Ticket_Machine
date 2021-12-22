from EN_interface import EN

def test_EN_interface_create_instance():
    EN()


def test_EN_interface_choice(monkeypatch):
    interface = EN()
    assert interface.text() == True