from json_saver import JSONSaver
from vacancy import Vacancy
from in_out import InOutController


def test_add_vacancy():
    with open('test.txt', 'r+') as f:
        f.truncate(0)
    vac = Vacancy(name='Manager', url='', from_=100000, to_=200000, currency='', requirements='dkdk')
    saver = JSONSaver('test.txt')
    saver.add_vacancy(str(vac))
    assert InOutController.get_from_file('test.txt') == ['Manager: 100000 - 200000 , dkdk\n']


def test_delete_vacancy():
    with open('test.txt', 'w+') as f:
        vac = Vacancy(name='Manager', url='', from_=100000, to_=200000, currency='', requirements='dkdk')
        saver = JSONSaver('test.txt')
        saver.add_vacancy(str(vac))
        saver.delete_vacancy(str(vac))
        assert InOutController.get_from_file('test.txt') == []