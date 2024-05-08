import psycopg2

from src.config import config


class DBManager:
    def __init__(self):
        self.db_name = 'hh_company'

    def execute_(self, query):
        conn = psycopg2.connect(dbname=self.db_name, **config())
        with conn:
            with conn.cursor() as cur:
                cur.execute(query)
                results = cur.fetchall()
        conn.close()
        return results


    def get_companies_and_vacancies_count(self):
        """Получает список всех компаний и количество вакансий у каждой компании."""
        result = self.execute_(f'SELECT companies.company_id, vacancies.company_name,'
                               f' COUNT(company_name) AS "Количество вакансий" '
                               f'FROM companies INNER JOIN vacancies '
                               f'USING (company_name) '
                               f'GROUP BY companies.company_id, vacancies.company_name '
                               f'ORDER BY company_id')
        return result