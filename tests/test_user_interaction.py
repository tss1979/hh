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

