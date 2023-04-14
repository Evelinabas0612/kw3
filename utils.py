import json
from datetime import datetime


def get_json():
    """
    функция загрузки json - файла
    :return: данные в виде json
    """
    try:
        with open('operations.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except FileNotFoundError as e:
        print(e, 'Отсутствует файл')


def filter_data(data):
    """
    функция, которая фильтрует данные из файла по state. Отбираются только со state = 'EXECUTED'.
    Все отобранные операции помещаются в новый список data_filter
    :param data:
    :return: data_filter
    """
    data_filter = []
    for row in data:
        if 'state' in row and row['state'] == 'EXECUTED':
            data_filter.append(row)
    return data_filter


def sort_data(data):
    """
    функция, которая сортирует по дате и времени операции. Возвращает 5 последних
    :param data:
    :return:data[:5]
    """
    data = sorted(data, key=lambda x: x['date'], reverse=True)
    return data[:5]


def format_data(data):
    """
    функция, которая форматирует полученные отсортированные данные в соответствии с требованиями:
    ### Требования

- Последние 5 выполненных (EXECUTED) операций выведены на экран.
- Операции разделены пустой строкой.
- Дата перевода представлена в формате ДД.ММ.ГГГГ (пример: 14.10.2018).
- Сверху списка находятся самые последние операции (по дате).
- Номер карты замаскирован и не отображается целиком в формате  XXXX XX** **** XXXX (видны первые 6 цифр и последние 4, разбито по блокам по 4 цифры, разделенных пробелом).
- Номер счета замаскирован и не отображается целиком в формате  **XXXX
(видны только последние 4 цифры номера счета).
    :param data:
    :return: data_format
    """
    data_format = []
    for row in data:
        date_format = datetime.strptime(row['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime("%d.%m.%Y")
        description_format = row['description']
        from_arrow = " "
        if 'from' in row:
            from_arrow = "->"
            sender_format = row['from'].split()
            sender_bill = sender_format.pop(-1)
            sender_info = " ".join(sender_format)
            sender_bill = f"{sender_bill[:4]} {sender_bill[4:6]}** **** {sender_bill[-4:]}"
        else:
            sender_info = "Новый счет"
            sender_bill = ""
            from_arrow = ""
        receiver_format = row['to'].split()
        receiver_bill = receiver_format.pop(-1)
        receiver_info = " ".join(receiver_format)
        receiver_bill = f"**{receiver_bill[-4:]}"
        amount_format = row['operationAmount']
        amount = amount_format['amount']
        currency_format = amount_format['currency']
        currency = currency_format['name']
        data_format.append(f"""
        {date_format} {description_format}
        {sender_info} {sender_bill} {from_arrow} {receiver_info} {receiver_bill}
        {amount} {currency}\
""")
    return data_format

