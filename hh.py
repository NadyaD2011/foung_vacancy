import requests
from general_function import predict_rub_salary_hh


def parse_hh_vacancies(language):
  url_hh = 'https://api.hh.ru/vacancies'
  vacancies_processed_hh = 0
  all_salary_hh = 0

  for page in range(20):
    params_hh = {
      'text': f'программист {language}',
      'area': 1,
      'period': 30,
      'per_page': 100,
      'page': page,
    }
    response = requests.get(url_hh, params=params_hh)
    response.raise_for_status()
    vacancies = response.json()
    for vacancy in vacancies['items']:
      salary = vacancy['salary']
      if salary and salary['currency'] == 'RUR':
        all_salary_hh += predict_rub_salary_hh(salary)
        vacancies_processed_hh += 1

  try:
    average_salary_hh = all_salary_hh/vacancies_processed_hh
  except ZeroDivisionError:
    average_salary_hh = 0

  date = {
    "vacancies_found": vacancies["found"],
    "vacancies_processed": vacancies_processed_hh,
    "average_salary": int(average_salary_hh),
  }

  return date