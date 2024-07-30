import os
import requests
from dotenv import load_dotenv
from draw_table import make_table
from general_function import get_statistics
from hh import parse_hh_vacancies
from sj import parse_superjob_vacancies


def main():
    load_dotenv()
    superjob_secret_key = os.getenv('SUPERJOB_SECRET_KEY')
    languages = ['Python', 'Java', 'JavaScript', 'C++', 'C#', 'C', 'Go', 'Scala', 'PHP', 'TypeScript']
    make_table(' SuperJob Moscow ', get_statistics(parse_superjob_vacancies, languages, superjob_secret_key))
    make_table(' HeadHunter Moscow ', get_statistics(parse_hh_vacancies, languages))

if __name__ == '__main__':
    main()