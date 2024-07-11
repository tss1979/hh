from exeptions import RangeException
from in_out import InOutController


class UserInteraction:
    QUERIES = {'hh': 'https://api.hh.ru/vacancies'}
    platforms: list = ["HeadHunter"]
    search_query: str
    top_n: int
    min_salary: float
    max_salary: float
    filter_words: list

    @staticmethod
    def check_range(salary_range: str):
        '''Функция поднимает исключение в случае некооректно переданного параметра range'''
        try:
            min_salary, max_salary = salary_range.split(' - ')
            min_salary = float(min_salary)
            max_salary = float(max_salary)
        except:
            raise RangeException('Неверный ввод диапозона зарплат')

    def check_search_query(self, key):
        '''Функция проверяет параметр ключа запроса'''
        if not isinstance(key, str):
            return False
        try:
            self.search_query = self.QUERIES[key]
            return True
        except KeyError:
            print('В данный момент сервис работает только с платформой  HeadHunter')
            return False

    @staticmethod
    def check_top_n(top_n):
        '''Функция проверяет корректность параметра количества вакансий'''
        try:
            int(top_n)
            return True
        except ValueError:
            print('Неправильный ввод количества вакансий')
            return False
        except TypeError:
            print('Неправильный ввод количества вакансий')
            return False

    def check_salary(self, salary_range):
        '''Функция проверяет корректность ввода диапазона зарплат'''
        try:
            self.check_range(salary_range)
            return True
        except RangeException:
            print('Неправильный ввод диапазона')
            return False

    def get_filter_words(self):
        '''Функция запрашивает параметр ключевых слов для поиска'''
        self.filter_words = input("Введите ключевые слова для фильтрации вакансий через пробел: ").split()

    def run(self):
        '''Функция запускает интерктив с пользователем'''
        while True:
            key = input("Введите ключ поискового запроса (для HeadHunter - hh): ").lower().strip()
            if self.check_search_query(key):
                break
        while True:
            top_n = input("Введите количество вакансий для вывода в топ N: ")
            if self.check_top_n(top_n):
                self.top_n = int(top_n)
                break
        self.get_filter_words()
        while True:
            salary_range = input("Введите диапазон зарплат (Пример: 100000 - 150000): ")
            if self.check_salary(salary_range):
                min_salary, max_salary = salary_range.split(' - ')
                self.min_salary = min(float(max_salary), float(max_salary))
                self.max_salary = max(float(max_salary), float(max_salary))
                break
        InOutController.load_vacancies(self.filter_words, self.search_query)






















