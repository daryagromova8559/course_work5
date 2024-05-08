from src.config import config
from src.utils import get_vacancies, create_database, save_data_to_database, get_company


def main():
    employee_ids = [
        '3403877',  # КСК
        '1998061',  # ООО Дары Артемиды
        '1102601',  # Самолет
        '1669803',  # ЗАО Русские протеины
        '3885811',  # ООО ТГК-2 Энергосбыт
        '612166',  # VIRTEX-FOOD
        '10932165',  # ООО Аврора
        '5516071',  # ООО Артэнерджи
    ]
    params = config()
    company_list = get_company(employee_ids)
    vacancy_list = get_vacancies(employee_ids)
    create_database('hh_company', params=params)
    save_data_to_database(company_list, vacancy_list, 'hh_company', params)


if __name__ == '__main__':
    main()