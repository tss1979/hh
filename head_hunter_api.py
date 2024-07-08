import requests


class HeadHunterAPI:
    url: str
    vacancies: list
    headers: dict = {'User-Agent': 'HH-User-Agent'}
    params: dict = {'text': '', 'page': 0, 'per_page': 100}

    def __init__(self, url):
        self.url = url
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []

    def get_vacancies(self, keywords: list) -> list:
        '''Функция принимает ключевые слова запроса, делает запрос к hh api
        и возвращеет список вакансий'''
        self.params['text'] = (' ').join(keywords)
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1
        return self.vacancies




