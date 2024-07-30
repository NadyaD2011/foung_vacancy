from terminaltables import DoubleTable


def make_table(name, vacancies_dict):
    table_data = [
        ['Язык программирования', 'Вакансий найдено', 'Вакансий обработано', 'Средняя зарплата'],
    ]
    for language, statistics in vacancies_dict.items():
        temp_data = [language]
        for value in statistics.values():
            temp_data.append(value)
        table_data.append(temp_data)
    table_instance = DoubleTable(make_table(vacancies_dict), name)
    print(table_instance.table)
    print()