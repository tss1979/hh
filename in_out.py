from head_hunter_api import HeadHunterAPI
from vacancy import Vacancy
from json_saver import JSONSaver


class InOutController:
    @staticmethod
    def load_vacancies(keywords: list, url: str) -> list:
        '''Функция принимает url запроса и ключевые слова и возвращает лист объектов Vacancy'''
        hh_api = HeadHunterAPI(url)
        hh_vacancies = hh_api.get_vacancies(keywords)
        return Vacancy.cast_to_object_list(hh_vacancies)

    @staticmethod
    def get_from_file(file_name: str) -> list:
        '''Функция принимает имя файла и возвращает список вакансий в строковом виде'''
        with open(file_name, 'r') as f:
            vacancies = f.readlines()
            return vacancies

    @staticmethod
    def print_vacancies(top_vacancies: list) -> None:
        '''Функция принимает список объектов Vacancy распечатывает построчно список вакансий
        в строковом виде'''
        for vacancy in top_vacancies:
            print(vacancy)

    @staticmethod
    def write_in_file(vacancies: list, file_name: str) -> None:
        '''Функция принимает список объектов Vacancy и имя файла и построчно записывает в файл'''
        saver = JSONSaver(file_name)
        for vacancy in vacancies:
            saver.add_vacancy(str(vacancy))



