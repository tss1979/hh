import pytest
from head_hunter_api import HeadHunterAPI

def test_get_vacancies():
    hh_api = HeadHunterAPI('https://api.hh.ru/vacancies')
    assert len(hh_api.get_vacancies(['Manager'])) > 0
    assert len(hh_api.get_vacancies('Manager')) > 0
    assert len(hh_api.get_vacancies('')) > 0
