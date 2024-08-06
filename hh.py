import requests
from general_function import predict_salary

def predict_rub_salary_for_hh(vacancy_info):
    if vacancy_info['salary'] and vacancy_info['salary']['currency'] == 'RUR':
        return predict_salary(vacancy_info['salary']['from'], vacancy_info['salary']['to'])
    

def parse_hh_vacancies(languages):
  hh_url = 'https://api.hh.ru/vacancies'
  param_settings = {'index_moscov': 1, 'public_period': 30, 'items_page': 100}
  params_hh = {
      'text': '',
      'area': param_settings['index_moscov'],
      'period': param_settings['public_period'],
      'per_page': param_settings['items_page'],
      'page': 0,
  }
        'vacancies_found': 0,
        'vacancies_processed': 0,
        'average_salary': 0,
  }

  for language_key in languages:
    params_hh['text'] = f'программист {language_key}'
    while params_hh['page'] < hh_pages:
      response = requests.get(hh_url, params=params_hh)
      response.raise_for_status()
      hh_response = response.json()
      language_section['vacancies_found'] = hh_response['found']
      all_vacancies += hh_response['items']
      hh_pages = hh_response['pages']
      params_hh['page'] += 1

    for vacancy in all_vacancies:
      job_salary = predict_rub_salary_for_hh(vacancy)
      if job_salary:
        language_section['vacancies_processed'] += 1
        language_section['average_salary'] += job_salary
    try:
      language_section['average_salary'] = int(language_section['average_salary'] / language_section['vacancies_processed'])
    except ZeroDivisionError:
       print('Ошибка деления на ноль')

    return language_section