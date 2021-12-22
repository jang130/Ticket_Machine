from english_interface import EN, WrongOptionError

def test_EN_interface_create_instance():
    EN()



def test_EN_interface_choice(monkeypatch):
    def choice():
        return '1'
    interface = EN()
    monkeypatch.setattr('english_interface.choice', choice)
    assert interface.text() is True
