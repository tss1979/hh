from vacancy import Vacancy


class VacancyController:

    @staticmethod
    def filter_vacancies(vacancies_list: list, filter_words: list) -> list:
        '''Функция принимает лист объектов Vacancy и лист слов запроса
        и отфильтровывает вакансии, которые содержат слова запроса в имени'''
        if len(filter_words) == 0:
            return vacancies_list
        if not isinstance(filter_words, list):
            return []
        result_list = []
        for vacancy in vacancies_list:
            result = False
            names = [name.lower() for name in vacancy.name.split()]
            for word in filter_words:
                if word.lower() in names:
                    result = True
            if result:
                result_list.append(vacancy)
        if len(result_list) == 0:
            print('Не найдены вакансии по заданным параметрам')
        return result_list

    @staticmethod
    def get_vacancies_by_salary(filtered_vacancies: list, min_: float, max_: float) -> list:
        '''Функция принимает лист объектов Vacancy, минимальный порог и максимальный порог
        и возвращает список вакансий отфилтрованных по минимальному и максимальному значению зарплаты'''
        if len(filtered_vacancies) == 0:
            print('Передан пустой массив')
            return []
        if isinstance(min_, float) and isinstance(max_, float) \
                and isinstance(filtered_vacancies[0], Vacancy):
            min_salary = [vac for vac in filtered_vacancies if vac.min_salary >= min_]
            result = [vac for vac in min_salary if vac.max_salary <= max_]
            return result
        else:
            print('Переданы неверные параметры')
            return []

    @staticmethod
    def sort_vacancies(ranged_vacancies: list) -> list:
        '''Функция принимает лист объектов Vacancy, и сортирует объекты по возрастанию
        минимальной зарплаты'''
        try:
            if isinstance(ranged_vacancies, list) and isinstance(ranged_vacancies[0], Vacancy):
                return list(sorted(ranged_vacancies, key=lambda x: x.min_salary, reverse=True))
            else:
                return []
        except IndexError:
            print('Передан пустой массив')

    @staticmethod
    def get_top_vacancies(sorted_vacancies: list, top_n: int):
        '''Функция принимает лист объектов Vacancy и количество объектов, которые нужно вернуть
        возращает лист объктов'''
        if isinstance(top_n, int) and isinstance(sorted_vacancies, list):
            return sorted_vacancies[:top_n]
        else:
            print('Введены некорректные данные')
            return []

