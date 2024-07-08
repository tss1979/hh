import pytest
from in_out import InOutController
from vacancy import Vacancy


def test_load_vacancies():
    assert len(InOutController.load_vacancies(['Python', 'Java'],'https://api.hh.ru/vacancies')) > 0
    assert len(InOutController.load_vacancies('', 'https://api.hh.ru/vacancies')) > 0


def test_get_from_file():
    with open('test.txt', 'r+') as f:
        f.truncate(0)
    vac = Vacancy(name='Manager', url='', from_=100000, to_=200000, currency='', requirements='dkdk')
    InOutController.write_in_file([vac], 'test.txt')
    assert InOutController.get_from_file('test.txt') == ['Manager: 100000 - 200000 , dkdk\n']


