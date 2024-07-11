import pytest
from in_out import InOutController
from vacancy import Vacancy

@pytest.fixture()
def vac_list():
    vac1 = Vacancy(name='Python blalaa', url='', from_=100000, to_=0, currency='', requirements='')
    vac2 = Vacancy(name='Python Java kdld', url='', from_=150000, to_=170000, currency='', requirements='')
    vac3 = Vacancy(name='Promfgng ggjg g gg', url='', from_=200000, to_=250000, currency='', requirements='')
    vac4 = Vacancy(name='Java', url='', from_=50000, to_=0, currency='', requirements='')
    return [vac1, vac2, vac3, vac4]

def test_load_vacancies():
    assert len(InOutController.load_vacancies(['Python', 'Java'],'https://api.hh.ru/vacancies')) > 0
    assert len(InOutController.load_vacancies('', 'https://api.hh.ru/vacancies')) > 0


def test_get_from_file():
    with open('test.txt', 'r+') as f:
        f.truncate(0)
    vac = Vacancy(name='Manager', url='', from_=100000, to_=200000, currency='', requirements='dkdk')
    InOutController.write_in_file([vac], 'test.txt')
    assert InOutController.get_from_file('test.txt') == ['Manager: 100000 - 200000 , dkdk\n']


def test_write_in_file(vac_list):
    InOutController.write_in_file(vac_list, 'test.txt')
    assert len(vac_list) == len(InOutController.get_from_file('test.txt'))





