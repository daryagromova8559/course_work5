import requests


def get_url(employee_id):
    """Поиск по названию"""
    try:
        params = {
            "per_page": 20,
            "employer_id": employee_id,
            "only_with_salary": True,
            "area": 113,
            "only_with_vacancies": True
        }
        r = requests.get("https://api.hh.ru/vacancies/", timeout=1, params=params)
        r.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error")
        print(errh.args[0])
        # Prints the response code
    return r.json()['items']


def get_company(employee_ids):
    '''Получение списка компаний'''
    company_list = []
    for employee_id in employee_ids:
        co_n = []
        co_url = []
        employee = get_url(employee_id)
        for company in employee:
            co_n.append(company['employer']['name'])
            co_url.append(company['employer']['url'])
        unique_company_name = set(co_n)
        unique_company_url = set(co_url)
        for company in unique_company_name:
            for url in unique_company_url:
                company_list.append({'companies': {'company_name': company, 'company_url': url}})
    return company_list