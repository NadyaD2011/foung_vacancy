def predict_salary(salary_from, salary_to):
  if salary_from and salary_to:
    return int((salary_from + salary_to)/2)
  elif salary_from:
    return int(salary_from*1.2)
  elif salary_to:
    return int(salary_to*0.8)
 

def get_statistics(agregator, languages, agregators_secret_key: str=None):
    statistic_of_languages = {}
    for language in languages:
        statistic_of_languages[language] = agregator(language, agregators_secret_key)

    return statistic_of_languages