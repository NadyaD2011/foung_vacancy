import requests
from general_function import predict_salary
  
def fetch_rub_salary_for_superJob(vacancy):
    if vacancy['currency'] == 'rub':
        return predict_salary(vacancy['payment_from'], vacancy['payment_to'])
    

def parse_superjob_vacancies(languages, superjob_secret_key):
  param_settings = {'index_moscov': 4, 'index_catalogues': 48, 'setting_salary': 1, 'count_results': 5}
  headers_sj = {
    'X-Api-App-Id': superjob_secret_key,
  }
  params_sj = {
      'page': 0,
      'count': param_settings['count_results'],
      'keyword': '',
      'town': param_settings['index_moscov'], 
      'catalogues': param_settings['index_catalogues'],
      'no_agreement': param_settings['setting_salary'],
  }
  sj_url = 'https://api.superjob.ru/2.0/vacancies/'
  superjob_pages = True
  all_vacancies = []
  vacancies_processed = 0

  for langeage_key in languages:
    params_sj['keyword'] = langeage_key
    while superjob_pages:
      response = requests.get(sj_url, headers=headers_sj, params=params_sj)
      response.raise_for_status()
      superjob_response = response.json()
      all_vacancies += superjob_response['objects']
      superjob_pages = superjob_response['more']
      params_sj['page'] += 1

    for vacancy in all_vacancies:
        job_salary = fetch_rub_salary_for_superJob(vacancy)
        if job_salary:
          vacancies_processed += 1
          average_salary += job_salary
          
    try:      
      average_salary = int(language_section['average_salary'] / language_section['vacancies_processed'])
    except ZeroDivisionError:
      average_salary = 0

    language_section = {
      "vacancies_found": superjob_response['total'],
      "vacancies_processed": vacancies_processed,
      "average_salary": average_salary,
    }
    
    return language_section