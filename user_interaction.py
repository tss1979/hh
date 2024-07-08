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

    def get_search_query(self):
        '''Функция запрашивает параметр ключа запроса и проверяет корректность'''
        while True:
            key = input("Введите ключ поискового запроса (для HeadHunter - hh): ").lower().strip()
            try:
                self.search_query = self.QUERIES[key]
                break
            except KeyError:
                print('В данный момент сервис работает только с платформой  HeadHunter')
                continue

    def get_top_n(self):
        '''Функция запрашивает параметр количества вакансий и проверяет корректность'''
        while True:
            try:
                top_n = int(input("Введите количество вакансий для вывода в топ N: "))
                self.top_n = top_n
                break
            except ValueError:
                print('Неправильный ввод количества вакансий')
                continue

    def get_salary(self):
        '''Функция преобразует переданный диапозон в значения минимальной и максимальной зарплаты'''
        while True:
            try:
                salary_range = input("Введите диапазон зарплат (Пример: 100000 - 150000): ")
                self.check_range(salary_range)
                min_salary, max_salary = salary_range.split(' - ')
                self.min_salary = min(float(max_salary), float(max_salary))
                self.max_salary = max(float(max_salary), float(max_salary))
                break
            except RangeException:
                print('Неправильный ввод диапазона')
                continue

    def get_filter_words(self):
        '''Функция запрашивает параметр ключевых слов для поиска'''
        self.filter_words = input("Введите ключевые слова для фильтрации вакансий через пробел: ").split()

    def run(self):
        '''Функция запускает интерктив с пользователем'''
        self.get_search_query()
        self.get_top_n()
        self.get_filter_words()
        self.get_salary()
        InOutController.load_vacancies(self.filter_words, self.search_query)






















