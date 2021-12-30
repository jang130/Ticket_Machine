from

def test_EN_interface_choice(monkeypatch):
    def choice():
        return '1'
    monkeypatch.setattr('english_interface.choice', choice)
    assert choice() == '1'

def test_EN_interface_options(monkeypatch):
    def choice():
        return '1'
    monkeypatch.setattr('english_interface.choice', choice)
    assert options(choice()) == True