import pytest
from vacancy_controler import VacancyController
from vacancy import Vacancy

@pytest.fixture()
def vac_list():
    vac1 = Vacancy(name='Python blalaa', url='', from_=100000, to_=0, currency='', requirements='')
    vac2 = Vacancy(name='Python Java kdld', url='', from_=150000, to_=170000, currency='', requirements='')
    vac3 = Vacancy(name='Promfgng ggjg g gg', url='', from_=200000, to_=250000, currency='', requirements='')
    vac4 = Vacancy(name='Java', url='', from_=50000, to_=0, currency='', requirements='')
    return [vac1, vac2, vac3, vac4]


def test_filter_vacancies(vac_list):
    assert len(VacancyController.filter_vacancies(vac_list, ['Java'])) == 2
    assert len(VacancyController.filter_vacancies(vac_list, ['Java', 'Python'])) == 3
    assert len(VacancyController.filter_vacancies(vac_list, [])) == 4
    assert len(VacancyController.filter_vacancies(vac_list, ['JS'])) == 0
    assert len(VacancyController.filter_vacancies(vac_list, 'JS')) == 0
    assert len(VacancyController.filter_vacancies(vac_list, 'Python')) == 0


def test_get_vacancies_by_salary(vac_list):
    assert len(VacancyController.get_vacancies_by_salary(vac_list, 200000, 250000)) == 1
    assert len(VacancyController.get_vacancies_by_salary(vac_list, 300000, 350000)) == 0
    assert len(VacancyController.get_vacancies_by_salary(vac_list, 100000, 0)) == 3


def test_sort_vacancies(vac_list):
    assert VacancyController.sort_vacancies(vac_list)[0].min_salary == max([v.min_salary for v in vac_list])
    assert VacancyController.sort_vacancies(vac_list)[-1].min_salary == min([v.min_salary for v in vac_list])


def test_get_top_vacancies(vac_list):
    assert len(VacancyController.get_top_vacancies(vac_list, 2)) == 2
    assert VacancyController.get_top_vacancies(vac_list, '2') == []
    assert VacancyController.get_top_vacancies([], 2) == []
    assert VacancyController.get_top_vacancies({}, 2) == []