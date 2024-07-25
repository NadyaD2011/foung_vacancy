# Сравниваем вакансии программистов

[HeadHunter](https://hh.ru) и [SuperJob](https://superjob.ru) - самые популярные площадки по поиску работы. Здесь публикуются тысячи вакансий работодателей и тысячи резюме соискателей.

## Описание:

Скрипт `main.py` скачивает вакансии по популярным языкам программирования с площадок `HH` и `SuperJob` за последний месяц. Считает среднюю зарплату популярного языка программирования и выводит в табличном виде.

## Окружение:
* Python 3.8+
* Пакетный менеджер `pip`


## Подготовка к запуску:
Для запуска скрипта установите [Python3](https://www.python.org/) `не ниже` версии `3.8`. Перейдите в каталог, куда скачали проект командой `cd` и сделайте следующее:

- Активируйте виртуальное окружение.
- Установите все зависимости для корректной работы скрипта.
```sh
python3 pip install -r requirements.txt
```
- Получите [токен](https://api.superjob.ru/) для взаимодействия с `API SuperJob`. Он будет: `v3.r.130948129.e3d78ebqz0f8ed7d609bcadfdd758963a44743e4.57b56cabf4ea0c8zf7eaa40fac59b23624ff41fb`. Присвойте его переменной `SUPERJOB_SECRET_KEY` и сохраните значение в файле с названием `.env` корня проекта.

## Пример запуска скрипта:
```sh
python3 main.py
```

## Лицензия:
Скрипт **main.py** находится под лицензией MIT. Его можно повторно использовать в проприетарном программном обеспечении при условии, что все копии лицензионного программного обеспечения включают копию условий лицензии MIT и уведомление об авторских правах.

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).