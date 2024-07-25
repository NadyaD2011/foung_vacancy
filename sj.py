import requests
from general_function import predict_rub_salary_sj
  

def parse_superjob_vacancies(language, superjob_secret_key):
  url_sj = 'https://api.superjob.ru/2.0/vacancies/'
  vacancies_processed_sj = 0
  all_salary_sj = 0

  for page in range(20):
    headers_sj = {
      'X-Api-App-Id': superjob_secret_key,
    }
    params_sj = {
        'page': page,
        'count': 5,
        'keyword': language,
        'town': 4, 
        'catalogues': 48,
        'no_agreement': 1,
    }

    response = requests.get(url_sj, headers=headers_sj, params=params_sj)
    response.raise_for_status()
    dictionary_professions = response.json()
    for vacancy in dictionary_professions["objects"]:
      if vacancy["currency"] == 'rub':
        all_salary_sj += predict_rub_salary_sj(vacancy)
        vacancies_processed_sj += 1

  try:
    average_salary_sj = all_salary_sj/vacancies_processed_sj
  except ZeroDivisionError:
    average_salary_sj = 0
  
  date = {
    "vacancies_found": dictionary_professions["total"],
    "vacancies_processed": vacancies_processed_sj,
    "average_salary": int(average_salary_sj),
  }

  return date