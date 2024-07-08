from vacancy import Vacancy
class JSONSaver:
    def __init__(self, file_name: str):
        self.file_name = file_name

    def add_vacancy(self, vacancy: Vacancy):
        '''Функция принимает объект Vacancy и записывает его в файл'''
        with open(self.file_name, 'a') as f:
            f.write(str(vacancy) + '\n')

    def delete_vacancy(self, vacancy: Vacancy):
        '''Функция принимает объект Vacancy и удаляет запись из файла'''
        with open(self.file_name, 'r') as f:
            vacancies = f.readlines()
            print(vacancies, vacancy)

        with open(self.file_name, 'w') as f:
            try:
                vacancies.remove(vacancy + '\n')
                if '\n' in vacancies:
                    vacancies.remove('\n')
            except:
                print('Нет такой вакансии')
            for vacancy in vacancies:
                f.write(vacancy + '\n')


