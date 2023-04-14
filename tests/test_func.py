import pytest
import os

from utils import filter_data, sort_data, format_data, get_json


# Создаем фикстуру, которая запускается перед каждым тестом
@pytest.fixture
def fixt_positive():  # имя фикстуры любое
    return [{
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }, {
        "id": 863064926,
        "state": "EXECUTED",
        "date": "2019-12-08T22:46:21.935582",
        "operationAmount": {
            "amount": "41096.24",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Открытие вклада",
        "to": "Счет 90424923579946435907"
    },
        {
            "id": 27192367,
            "state": "CANCELED",
            "date": "2018-12-24T20:16:18.819037",
            "operationAmount": {
                "amount": "991.49",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 71687416928274675290",
            "to": "Счет 87448526688763159781"
        }
    ]


def test_get_json_positive():
    data = get_json('test_operations.json')
    assert len(data) == 3
    assert data == [{
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }, {
        "id": 863064926,
        "state": "EXECUTED",
        "date": "2019-12-08T22:46:21.935582",
        "operationAmount": {
            "amount": "41096.24",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Открытие вклада",
        "to": "Счет 90424923579946435907"
    },
        {
            "id": 27192367,
            "state": "CANCELED",
            "date": "2018-12-24T20:16:18.819037",
            "operationAmount": {
                "amount": "991.49",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 71687416928274675290",
            "to": "Счет 87448526688763159781"
        }
    ]

    new_data = get_json('file_is_absent.json')
    assert new_data == "Не удается найти указанный файл"


def test_filter_data(fixt_positive):
    fixt_positive_filter = filter_data(fixt_positive)
    assert [x['state'] for x in fixt_positive_filter] == ["EXECUTED", "EXECUTED"]


def test_sort_data(fixt_positive):
    fixt_positive_sort = sort_data(fixt_positive)
    assert [x['date'] for x in fixt_positive_sort] == ["2019-12-08T22:46:21.935582", "2019-08-26T10:50:58.294041",
                                                       "2018-12-24T20:16:18.819037"]


def test_format_data(fixt_positive):
    fixt_positive_format = format_data(fixt_positive)
    assert [fixt_positive_format] == [['\n'
                                       '        26.08.2019 Перевод организации\n'
                                       '        Maestro 1596 83** **** 5199 -> Счет **9589\n'
                                       '        31957.58 руб.',
                                       '\n'
                                       '        08.12.2019 Открытие вклада\n'
                                       '        Новый счет   Счет **5907\n'
                                       '        41096.24 USD',
                                       '\n'
                                       '        24.12.2018 Перевод со счета на счет\n'
                                       '        Счет 7168 74** **** 5290 -> Счет **9781\n'
                                       '        991.49 руб.']]
