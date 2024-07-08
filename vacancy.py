
class Vacancy:
    name: str
    url: str
    min_salary: float
    max_salary: float
    requirements: str
    currency: str

    def __init__(self, name, url, from_, to_, currency, requirements):
        self.name = name
        self.url = url
        self.min_salary = from_
        self.max_salary = to_
        self.currency = currency
        self.requirements = requirements


    @staticmethod
    def get_salary(range_):
        min_salary, max_salary = range_.split(' - ')
        min_salary = int(min_salary)
        max_salary = int(max_salary)
        min_salary = min(min_salary, max_salary)
        max_salary = max(min_salary, max_salary)
        return min_salary, max_salary

    @staticmethod
    def cast_to_object_list(hh_vacancies: list) -> list:
        '''Функция преобразования набора данных из JSON в список объектов'''
        vacancies = []
        for vacancy in hh_vacancies:
            try:
                name = vacancy.get('name', '')
                url = vacancy.get('url', '')
                requirements = vacancy.get('snippet', {}).get('requirement', '')
                from_ = vacancy.get('salary', {}).get('from', 0)
                to_ = vacancy.get('salary', {}).get('to', 0)
                currency = vacancy.get('salary', {}).get('currency', '')
                from_ = from_ if from_ else 0
                to_ = to_ if to_ else 0
            except AttributeError:
                continue
            else:
                vacancy = Vacancy(name, url, from_, to_, currency, requirements)
                vacancies.append(vacancy)
        return vacancies

    def __str__(self):
        max_block = f' - {self.max_salary}' if self.max_salary != 0 else ''
        return f'{self.name.title()}: {self.min_salary}{max_block} {self.currency}, {self.requirements}'


