import pytest
from user_interaction import UserInteraction
from exeptions import RangeException


def test_check_range_exception():
    with pytest.raises(RangeException) as e:
        UserInteraction.check_range('')
    assert "Неверный ввод диапозона зарплат" in str(e.value)

    with pytest.raises(RangeException) as e:
        UserInteraction.check_range('444')
    assert "Неверный ввод диапозона зарплат" in str(e.value)

    with pytest.raises(RangeException) as e:
        UserInteraction.check_range('444 555')
    assert "Неверный ввод диапозона зарплат" in str(e.value)

    with pytest.raises(RangeException) as e:
        UserInteraction.check_range('ff - fff')
    assert "Неверный ввод диапозона зарплат" in str(e.value)


def test_check_search_query():
    ui = UserInteraction()
    assert ui.check_search_query('hh') is True
    assert ui.check_search_query('') is False
    assert ui.check_search_query('avito') is False
    assert ui.check_search_query({}) is False
    assert ui.check_search_query([]) is False


def test_check_top_n():
    ui = UserInteraction()
    assert ui.check_top_n('2') is True
    assert ui.check_top_n(2) is True
    assert ui.check_top_n('') is False
    assert ui.check_top_n({}) is False
    assert ui.check_top_n([]) is False


def test_check_salary():
    ui = UserInteraction()
    assert ui.check_salary('100 - 200') is True
    assert ui.check_salary('100.34 - 100.89') is True
    assert ui.check_salary('100 200') is False
    assert ui.check_salary('') is False
    assert ui.check_salary([]) is False
    assert ui.check_salary({}) is False