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
