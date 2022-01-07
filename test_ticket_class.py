from ticket_class import ticket
import pytest


def test_ticket_class():
    ticket((1, '20min', '00:01:56 05/01/2022'))


def test_ticket_class_to_less_atributes():
    with pytest.raises(ValueError):
        ticket((1, '20min'))


def test_ticket_class_to_many_atributes():
    with pytest.raises(ValueError):
        ticket((1, '20min', '00:01:56 05/01/2022', 1))
