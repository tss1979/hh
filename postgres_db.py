import psycopg2
from config import config
from vacancy import Vacancy


class PostgresDB:
    def __init__(self):
        self.params = config()
        self.conn = psycopg2.connect(dbname='hh', **self.params)
        self.cur = self.conn.cursor()

    def create_table(self, table_name: str) -> None:
        '''Функция создает таблицы работодателей или вакансий'''
        with self.conn:
            if table_name == 'employers':
                self.cur.execute(f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255));""")
            elif table_name == 'vacancies':
                self.cur.execute(f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                id SERIAL PRIMARY KEY,
                employer_id INT REFERENCES employers(id),
                name VARCHAR(255),
                salary INT,
                url VARCHAR(255),
                requirements TEXT);""")
            else:
                raise ValueError('Wrong table name')

    def insert_data(self, vacancies: list) -> None:
        '''Функция заполняет таблицы баы данных полученными данными'''
        with self.conn:
            for vac in vacancies:
                self.cur.execute("INSERT INTO public.employers (name) VALUES (%s) RETURNING id", (vac.employer,))
                emp_id = self.cur.fetchone()[0]
                self.cur.execute("""INSERT INTO public.vacancies (employer_id, name, salary, url, requirements)
                 VALUES (%s, %s, %s, %s, %s)""", (emp_id, vac.name, int(vac.min_salary), vac.url, vac.requirements))
