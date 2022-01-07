from customer_class import customer
import pytest


def test_ticket_class():
    customer(('1', 'Doralyn', 'Dovermann', '1', '100000'))


def test_ticket_class_to_less_atributes():
    with pytest.raises(ValueError):
        customer(('1', 'Doralyn', 'Dovermann', '1'))


def test_ticket_class_to_many_atributes():
    with pytest.raises(ValueError):
        customer(('1', 'Doralyn', 'Dovermann', '1', '100000', '1'))
